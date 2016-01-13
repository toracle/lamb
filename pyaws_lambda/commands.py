# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
from botocore.exceptions import ClientError

from . import CONFIG_PROJECT, DIST_PACKAGE_FILENAME, DIST_PACKAGE_DIR, LAMBDA_CLIENT, MODULES_DIR
from .resources import Lambda
from .zip_utils import zip_dir


def deploy_functions():
    functions_info = CONFIG_PROJECT.get('functions')
    with file(DIST_PACKAGE_FILENAME, 'rb') as zfin:
        code = zfin.read()
    lambda_functions = Lambda.load_functions(LAMBDA_CLIENT, functions_info)
    for lambda_function in lambda_functions:
        try:
            lambda_function.code = {'ZipFile': code}
            lambda_function.create_function()
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ResourceConflictException':
                lambda_function.update_function_code()


def make_dist_package():
    if not os.path.exists(DIST_PACKAGE_DIR):
        os.makedirs(DIST_PACKAGE_DIR)
    zip_dir(DIST_PACKAGE_FILENAME, MODULES_DIR)


def install_requirements():
    pass


def copy_modules_to_dist_dir():
    pass
