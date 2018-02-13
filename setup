#!/usr/bin/env python

from setuptools import setup
from plantuml import __author__, __version_string__, __email__

#
# Release process
#
# Setup:
# vim ~/.pypirc
# .pypirc file contents
#
# [distutils]
# index-servers =
#   pypi
#   pypitest
#
# [pypi]
# username: YOUR_USERNAME_HERE
# password: YOUR_PASSWORD_HERE
#
# [pypitest]
# username: YOUR_USERNAME_HERE
# password: YOUR_PASSWORD_HERE
#
# Run this to build the `dist/PACKAGE_NAME-xxx.tar.gz` file
#     python setup.pyc sdist
#
# Run this to build & upload it to `pypi`:
#     python setup.pyc sdist upload -r pypi
#


setup(
    name='plantuml_connection',
    version=__version_string__,
    description='',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/evandroforks/PlantUmlConnection',
    author=__author__,
    author_email=__email__,
    license='BSD',
    package_dir = {'': 'all'},
    packages = [
    ],
    install_requires=[
    ],
    py_modules=['plantuml_connection'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['plantuml_connection', 'uml']
)
