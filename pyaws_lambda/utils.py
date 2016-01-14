# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from yaml import load as yaml_load


def read_yaml_config(path):
    with file(path) as fin:
        content = fin.read()
        return yaml_load(content)


def camelcase_to_underscore(s):
    new_str = ''
    for index, char in enumerate(s):
        if char.isupper() and index != 0:
            new_str += '_{}'.format(char.lower())
        elif char.isupper():
            new_str += char.lower()
        else:
            new_str += char
    return new_str


def set_dict_to_instance(d, instance, args, args_with_default):
    for arg in args:
        setattr(instance, arg, d[arg])

    for arg, default in args_with_default.items():
        setattr(instance, arg, d.get(arg, default))
