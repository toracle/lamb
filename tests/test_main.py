# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
from pyaws_lambda import Context
from pyaws_lambda.commands import make_dist_package
from pyaws_lambda.commands import deploy_functions


'''
def test_make_dist_package():
    context = Context.default_context(
        PATH_URLS_YAML=os.path.join('tests', 'urls.yaml'),
        PATH_PROJECT_YAML=os.path.join('tests', 'project.yaml'),
        MODULES_DIR=os.path.join('tests', 'modules')
    )
    make_dist_package(context)
    deploy_functions(context)
    assert True
'''

