# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

__version__ = "0.1.0"

from .utils import read_yaml_config

PATH_URLS_YAML = 'urls.yaml'
PATH_PROJECT_YAML = 'project.yaml'
DIST_PACKAGE_DIR = 'dists'
DIST_PACKAGE_FILENAME = 'dists.zip'
MODULES_DIR = 'modules'

LAMBDA_CLIENT = boto3.client('lambda')

CONFIG_URLS = read_yaml_config(PATH_URLS_YAML)
CONFIG_PROJECT = read_yaml_config(PATH_PROJECT_YAML)
