# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

__version__ = "0.1.0"

import sys
import os
from . import commands
from .utils import read_yaml_config
import boto3


class Context(dict):
    @staticmethod
    def default_context(**kwargs):
        context = Context()

        context['PATH_URLS_YAML'] = kwargs.get('PATH_URLS_YAML', 'urls.yaml')
        context['PATH_PROJECT_YAML'] = kwargs.get('PATH_PROJECT_YAML', 'project.yaml')
        context['DIST_PACKAGE_DIR'] = kwargs.get('DIST_PACKAGE_DIR', 'dists')
        context['DIST_PACKAGE_FILENAME'] = kwargs.get('DIST_PACKAGE_FILENAME', 'dists.zip')
        context['MODULES_DIR'] = kwargs.get('MODULES_DIR', 'modules')

        context['CONFIG_PROJECT'] = read_yaml_config(context['PATH_PROJECT_YAML'])
        try:
            context['CONFIG_URLS'] = read_yaml_config(context['PATH_URLS_YAML'])
        except IOError:
            context['CONFIG_URLS'] = {}

        context['LAMBDA_CLIENT'] = boto3.client('lambda')
        return context


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    try:
        #cmd_name, cmd_args = parseopts(args)
        pass
    except Exception as exc:
        sys.stderr.write('ERROR: {}'.format(exc))
        sys.stderr.write(os.linesep)
        sys.exit(1)

    context = Context.default_context()
    commands.make_dist_package(context)
    commands.deploy_functions(context)
