# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import boto3
from botocore.exceptions import ClientError


class Lambda(object):
    def __init__(self):
        self.boto_params = ['FunctionName', 'Role', 'Handler', 'Code', 'Publish', 'Description', 'Runtime', 'Timeout', 'MemorySize']
        self.client = None
        self.function_name = None
        self.role = None
        self.handler = None
        self.code = None
        self.publish = None
        self.description = ''
        self.runtime = 'python2.7'
        self.timeout = 3
        self.memory_size = 128

    @staticmethod
    def _load_each_function(client, function_info):
        lambda_function = Lambda()
        lambda_function.client = client

        set_dict_to_instance(function_info,
                             lambda_function,
                             ['function_name', 'role', 'handler', 'publish'],
                             {'description': '', 'runtime': 'python2.7', 'timeout': 3, 'memory_size': 128})
        return lambda_function
        
    @staticmethod
    def load_functions(client, function_info):
        _type = type(function_info)
        
        if _type == dict:
            return [Lambda._load_each_function(client, function_info)]
        elif _type == tuple or _type == list:
            return [Lambda._load_each_function(client, _info) for _info in function_info]
        
    def create_function(self):
        params = dict([(arg, getattr(self, camelcase_to_underscore(arg))) for arg in self.boto_params])
        self.client.create_function(**params)

    def update_function_code(self):
        params = {'FunctionName': self.function_name, 'ZipFile': self.code['ZipFile'], 'Publish': self.publish}
        self.client.update_function_code(**params)
