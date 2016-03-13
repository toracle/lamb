# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys

import lamb
from lamb import commands
from lamb import exceptions

if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)


def main(args=None):
    try:
        context = lamb.Context.default_context()
        commands.make_dist_package(context)
        commands.deploy_functions(context)
    except exceptions.ConfigurationInvalidException as e:
        print(e)


if __name__ == '__main__':
    sys.exit(main(args=sys.argv))
