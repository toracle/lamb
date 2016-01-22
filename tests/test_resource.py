# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
from pyaws_lambda import Context
from pyaws_lambda.resources import API
from pyaws_lambda.resources import Lambda
from pyaws_lambda.resources import Project


def test_load_lambda_meta():
    context = Context.default_context(
        PATH_URLS_YAML=os.path.join('tests', 'urls.yaml'),
        PATH_PROJECT_YAML=os.path.join('tests', 'project.yaml'),
        MODULES_DIR=os.path.join('tests', 'modules')
    )

    project_name = context['CONFIG_PROJECT'].get('project_name')
    project = Project.make_project(None, project_name)

    lambda_meta = context['CONFIG_PROJECT'].get('functions')
    lambda_list = Lambda.load_functions(project, lambda_meta)

    assert len(lambda_list) == 2

    l0 = lambda_list[0]
    assert l0.function_name == 'series'
    assert l0.role == 'arn:aws:iam::role'
    assert l0.handler == 'series.json'
    assert l0.publish is True
    assert l0.description == ''

    l1 = lambda_list[1]
    assert l1.function_name == 'hello'
    assert l1.role == 'arn:aws:iam::role'
    assert l1.handler == 'hello.say'
    assert l1.publish is True
    assert l1.description == ''


def test_load_api_meta():
    context = Context.default_context(
        PATH_URLS_YAML=os.path.join('tests', 'urls.yaml'),
        PATH_PROJECT_YAML=os.path.join('tests', 'project.yaml'),
        MODULES_DIR=os.path.join('tests', 'modules')
    )

    project_name = context['CONFIG_PROJECT'].get('project_name')
    project = Project.make_project(None, project_name)

    api_meta = context['CONFIG_PROJECT'].get('urls')
    api_list = API.load_urls(project, api_meta)

    assert len(api_list) == 2

    for api in api_list:
        assert api.path in ['/series', '/hello']
        assert api.method == 'GET'
        assert api.function_name in ['series', 'hello']
