# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from pyaws_lambda.utils import camelcase_to_underscore

def test_camelcase_to_underscore():
    assert camelcase_to_underscore('FunctionName') == 'function_name'
    assert camelcase_to_underscore('Host') == 'host'
    assert camelcase_to_underscore('CamelcaseToUnderscore') == 'camelcase_to_underscore'
