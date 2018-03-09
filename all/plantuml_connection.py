#!/usr/bin/env python

from argparse import ArgumentParser
from os import environ, path, makedirs
from zlib import compress

from urllib.request import Request, urlopen


__version__ = 1, 0, 3
__version_string__ = '.'.join(str(x) for x in __version__)

__author__ = 'Doug Napoleone, Samuel Marks, Evandro Coan'
__email__ = 'doug.napoleone+plantuml@gmail.com'


class PlantUMLError(Exception):
    """
    Error in processing.
    """
    pass


class PlantUMLConnectionError(PlantUMLError):
    """
    Error connecting or talking to PlantUML Server.
    """
    pass


class PlantUMLHTTPError(PlantUMLConnectionError):
    """
    Request to PlantUML server returned HTTP Error.
    """

    def __init__(self, response, content, *args, **kwdargs):
        super(PlantUMLConnectionError, self).__init__(*args, **kwdargs)
        self.response = response
        self.content = content
        if not self.message:
            self.message = "%d: %s" % (
                self.response.status, self.response.reason)


class PlantUMLSyntaxError(PlantUMLError):

    def __init__(self, http_headers, *args, **kwdargs):
        super(PlantUMLError, self).__init__(*args, **kwdargs)
        self.http_headers = http_headers

    def __str__(self):
        return str( self.http_headers ).strip('\n')


def deflate_and_encode(plantuml_text):
    """zlib compress the plantuml text and encode it for the plantuml server.
    """
    zlibbed_str = compress(plantuml_text)
    compressed_string = zlibbed_str[2:-4]
    return encode(compressed_string)


def encode(data):
    """encode the plantuml data which may be compresses in the proper
    encoding for the plantuml server
    """
    res = ""
    for i in range(0, len(data), 3):
        if i + 2 == len(data):
            res += _encode3bytes(data[i], data[i + 1], 0)
        elif i + 1 == len(data):
            res += _encode3bytes(data[i], 0, 0)
        else:
            res += _encode3bytes(data[i], data[i + 1], data[i + 2])
    return res


def _encode3bytes(b1, b2, b3):
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    res = ""
    res += _encode6bit(c1 & 0x3F)
    res += _encode6bit(c2 & 0x3F)
    res += _encode6bit(c3 & 0x3F)
    res += _encode6bit(c4 & 0x3F)
    return res


def _encode6bit(b):
    if b < 10:
        return chr(48 + b)
    b -= 10
    if b < 26:
        return chr(65 + b)
    b -= 26
    if b < 26:
        return chr(97 + b)
    b -= 26
    if b == 0:
        return '-'
    if b == 1:
        return '_'
    return '?'


class PlantUML(object):
    """Connection to a PlantUML server with optional authentication.

    All parameters are optional.

    :param str url: URL to the PlantUML server image CGI.
    """

    def __init__(self, url):
        self.url = url

    def get_url(self, plantuml_text):
        """Return the server URL for the image.
        You can use this URL in an IMG HTML tag.

        :param str plantuml_text: The plantuml markup to render
        :returns: the plantuml server image URL
        """
        return self.url + deflate_and_encode(plantuml_text)

    def processes(self, plantuml_text):
        """Processes the plantuml text into the raw PNG image data.

        :param str plantuml_text: The plantuml markup to render
        :returns: the raw image data
        """
        url = self.get_url(plantuml_text)
        try:
            request = Request(url)
            openurl = urlopen(request)
            http_headers = openurl.info()

        except Exception as error:
            raise PlantUMLConnectionError(error)

        # print( "http_headers: %s" % http_headers )
        if "X-PlantUML-Diagram-Error" in http_headers:
            raise PlantUMLSyntaxError( http_headers )

        else:
            content = openurl.read()

        if openurl.getcode() != 200:
            raise PlantUMLHTTPError(openurl.getcode(), content)

        return content

    def processes_file(self, filename, outfile=None, errorfile=None, directory=''):
        """Take a filename of a file containing plantuml text and processes
        it into a .png image.

        :param str filename: Text file containing plantuml markup
        :param str outfile: Filename to write the output image to. If not
                    supplied, then it will be the input filename with the
                    file extension replaced with '.png'.
        :param str errorfile: Filename to write server html error page
                    to. If this is not supplined, then it will be the
                    input ``filename`` with the extension replaced with
                    '_error.html'.
        :returns: ``True`` if the image write succedded, ``False`` if there was
                    an error written to ``errorfile``.
        """
        if outfile is None:
            outfile = path.splitext(filename)[0] + '.png'
        if errorfile is None:
            errorfile = path.splitext(filename)[0] + '_error.html'
        if directory and not path.exists(directory):
            makedirs(directory)
        with open(filename, 'rb') as filedata:
            data = filedata.read()
        try:
            content = self.processes(data)
        except PlantUMLHTTPError as e:
            err = open(path.join(directory, errorfile), 'w')
            err.write(e.content)
            err.close()
            return False
        out = open(path.join(directory, outfile), 'wb')
        out.write(content)
        out.close()
        return True


def _build_parser():
    default_server_url = 'http://www.plantuml.com/plantuml/png/'
    parser = ArgumentParser(description='Generate images from plantuml defined files using plantuml server')
    parser.add_argument('files', metavar='filename', nargs='+',
                        help='file(s) to generate images from')
    parser.add_argument('-o', '--out', default='',
                        help='directory to put the files into')
    parser.add_argument('-s', '--server', default=default_server_url,
                        help='server to generate from, defaults to "%s"' % default_server_url)
    return parser


def main():
    args = _build_parser().parse_args()
    plantumlserver = PlantUML(args.server)

    for filename in args.files:
        print("filename: %s, gen_success: %s" % (filename, plantumlserver.processes_file(filename, directory=args.out)))


if __name__ == '__main__':
    main()

