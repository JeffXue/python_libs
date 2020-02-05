#!/usr/bin/env python3.7

import os


def is_path_exist(path):
    if not os.path.exists(path):
        return False
    return True


def is_path_empty(path):
    if len(os.listdir(path)) == 0:
        return True
    return False
