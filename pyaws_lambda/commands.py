# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
from botocore.exceptions import ClientError

from .resources import Lambda
from .resources import Project
from .zip_utils import zip_dir
from .utils import read_binary


def deploy_functions(context):
    client = context['LAMBDA_CLIENT']
    project_name = context['CONFIG_PROJECT'].get('project-name')
    functions_info = context['CONFIG_PROJECT'].get('functions')
    code = read_binary(context['DIST_PACKAGE_FILENAME'])

    project = Project.make_project(client, project_name)

    for lambda_function in Lambda.load_functions(project, functions_info):
        try:
            lambda_function.code = {'ZipFile': code}
            lambda_function.create_function()
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ResourceConflictException':
                lambda_function.update_function_code()


def make_dist_package(context):
    if not os.path.exists(context['DIST_PACKAGE_DIR']):
        os.makedirs(context['DIST_PACKAGE_DIR'])
    zip_dir(context['DIST_PACKAGE_FILENAME'], context['MODULES_DIR'])


def install_requirements(context):
    pass


def copy_modules_to_dist_dir(context):
    pass
