# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import boto3
from botocore.exceptions import ClientError
from .utils import set_dict_to_instance
from .utils import camelcase_to_underscore


class Project(object):
    def __init__(self, client, name):
        self.client = client
        self.name = name

    @staticmethod
    def make_project(client, name):
        return Project(client, name)

    def create_function(self, function_meta):
        return Lambda.load_functions(self, function_meta)


class Lambda(object):
    def __init__(self):
        self.boto_params = ['FunctionName', 'Role', 'Handler', 'Code', 'Publish', 'Description', 'Runtime', 'Timeout', 'MemorySize']
        self.project = None
        self.function_name = None
        self.role = None
        self.handler = None
        self.code = {}
        self.publish = None
        self.description = ''
        self.runtime = 'python2.7'
        self.timeout = 3
        self.memory_size = 128

    @staticmethod
    def _load_each_function(project, function_meta):
        lambda_function = Lambda()
        lambda_function.project = project

        set_dict_to_instance(function_meta,
                             lambda_function,
                             ['function_name', 'role', 'handler', 'publish'],
                             {'description': '', 'runtime': 'python2.7', 'timeout': 3, 'memory_size': 128})
        return lambda_function

    @staticmethod
    def load_functions(project, function_meta):
        _type = type(function_meta)

        if _type == dict:
            return [Lambda._load_each_function(project, function_meta)]
        elif _type == tuple or _type == list:
            return [Lambda._load_each_function(project, _info) for _info in function_meta]

    def get_canonical_function_name(self):
        return "{}--{}".format(self.project.name, self.function_name)

    def create_function(self):
        params = dict([(arg, getattr(self, camelcase_to_underscore(arg))) for arg in self.boto_params])
        params['FunctionName'] = self.get_canonical_function_name()
        self.project.client.create_function(**params)

    def update_function_code(self):
        params = {'FunctionName': self.get_canonical_function_name(), 'ZipFile': self.code['ZipFile'], 'Publish': self.publish}
        self.project.client.update_function_code(**params)
