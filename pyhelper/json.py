#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from json import (load, dump)
from os.path import isfile
from typing import Union


class Json:
    """
    Read/write from/to json format
    """

    ##################################################

    @staticmethod
    def read(file_path: str) -> list:
        """
        read
        """
        if not isinstance(file_path, str):
            raise TypeError('file_path must be set to a string')
        if not file_path:
            raise ValueError('file_path cannot be empty')
        if not isfile(file_path):
            raise OSError('file doe not exist')
        data = None
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = load(json_file)
        except Exception as e:
            raise e
        finally:
            return data

    ##################################################

    @staticmethod
    def write(data: Union[list, dict], file_path: str) -> None:
        """
        write
        """
        if not isinstance(data, list) and not isinstance(data, dict):
            raise TypeError('data must be set to a list or a dictionary')
        if not isinstance(file_path, str):
            raise TypeError('file_path must be set to a string')
        if not file_path:
            raise ValueError('file_path cannot be empty')
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                dump(data, json_file)
        except Exception as e:
            raise e


##################################################


if __name__ == '__main__':
    pass
