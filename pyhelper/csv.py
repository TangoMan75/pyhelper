#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from csv import (reader, DictWriter)
from os.path import isfile
from typing import List


class CSV:
    """
    Read/write from/to csv files
    NOTE: csv file MUST have header row and every item will be casted as a string
    https://docs.python.org/3/library/csv.html
    https://docs.python.org/3/library/os.path.html#os.path.isfile
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
        fieldnames = []
        data = []
        try:
            with open(file_path, 'r', encoding='utf-8', newline='') as csv_file:
                flag = True
                for row in reader(csv_file):
                    if flag:
                        fieldnames = row
                        flag = False
                    else:
                        index = 0
                        item = {}
                        for temp in row:
                            item[fieldnames[index]] = temp
                            index += 1
                        data.append(item)
        except Exception as e:
            raise e
        finally:
            return data

    ##################################################

    @staticmethod
    def write(data: List[dict], file_path: str) -> None:
        """
        write
        """
        if not isinstance(file_path, str):
            raise TypeError('file_path must be set to a string')
        if not file_path:
            raise ValueError('file_path cannot be empty')
        if not isinstance(data, list):
            raise TypeError('data must be set to a list')
        if data == []:
            raise ValueError('data cannot be empty')
        if not isinstance(data[0], dict):
            raise TypeError('data must contain a list of dictionaries')
        if len(data[0]) == 0:
            raise ValueError('data cannot contain empty dictionaries')
        try:
            with open(file_path, 'w', encoding='utf-8', newline='') as csv_file:
                writer = DictWriter(csv_file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            raise e


##################################################


if __name__ == '__main__':
    pass
