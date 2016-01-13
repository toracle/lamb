# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import zipfile


def zip_dir(filename, target_dir):
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as z_fout:
        basedir_index = len(target_dir) + 1
        for base, _, files in os.walk(target_dir):
            for f in files:
                filename = os.path.join(base, f)
                z_fout.write(filename, filename[basedir_index:])
