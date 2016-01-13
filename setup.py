#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages
from codecs import open

def read(*names, **kwargs):
    with open(os.path.join(os.path.dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf-8')) as fin:
        return fin.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

version = find_version("pyaws_lambda", "__init__.py")
long_description = read('README.rst', encoding='utf-8')

setup(
    name='pyaws_lambda',
    version=version,
    description='Server stack with AWS Lambda',
    url='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['pyyaml', 'boto3'],
)
