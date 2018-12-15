#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys

from setuptools import setup

sys.path.append(os.path.join(os.path.dirname(__file__), 'all'))
from all.plantuml_connection import __author__, __version_string__, __email__


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
#     python setup.py sdist
#
# Run this to build & upload it to `pypi`:
#     python setup.py sdist upload -r pypi
#

setup(
    name='plantuml_connection',
    version=__version_string__,
    description='',
    long_description=open('README.md').read(),
    url='https://github.com/evandroforks/plantumlconnection',
    author=__author__,
    author_email=__email__,
    license='BSD',
    package_dir = {'': 'all'},
    packages = [
        'plantuml_connection'
    ],
    install_requires=[
    ],
    data_files = [
        ("", ["LICENSE.txt"]),
    ],
    py_modules=['plantuml_connection'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
