#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

import logging
from os import (rename, mkdir, pardir)
from os.path import join, exists, abspath
from re import sub
from typing import Optional
from unicodedata import normalize, category


class Renamer:
    """
    Renamer
    """

    def __init__(self, source: Optional[str] = None, destination: Optional[str] = None):
        self._source = None
        self._destination = None
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination

    ##################################################
    # source Setter / Getter
    ##################################################

    @property
    def source(self) -> Optional[str]:
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        if not isinstance(source, str):
            raise TypeError(f'{self.__class__.__name__}.source must be set to a string, {type(source)} given')
        if source == '':
            raise ValueError(f'{self.__class__.__name__}.source cannot be empty')
        if not exists(source):
            raise ValueError(f'{self.__class__.__name__}.source must be set to a valid path')
        self._source = source
        # when not defined destination is same source folder
        if self._destination is None:
            self._destination = abspath(join(self._source, pardir))

    ##################################################
    # destination Setter / Getter
    ##################################################

    @property
    def destination(self) -> Optional[str]:
        return self._destination

    @destination.setter
    def destination(self, destination: Optional[str]) -> None:
        if not isinstance(destination, str):
            raise TypeError(f'{self.__class__.__name__}.destination must be set to a string, {type(destination)} given')
        if destination == '':
            raise ValueError(f'{self.__class__.__name__}.destination cannot be empty')
        if not exists(destination):
            raise ValueError(f'{self.__class__.__name__}.destination must be set to a valid path')
        self._destination = destination

    ##################################################

    def rename(self, new_basename: str) -> None:
        if not isinstance(new_basename, str):
            raise TypeError(
                f'{self.__class__.__name__}.new_basename must be set to a string, {type(new_basename)} given')
        if new_basename == '':
            raise ValueError(f'{self.__class__.__name__}.new_basename cannot be empty')
        # create destination when not found
        if not exists(self._destination):
            try:
                mkdir(self._destination)
            except OSError:
                raise OSError(f'Failed creating directory: {self._destination}')
            else:
                logging.debug('Creating folder: ' + self._destination)
        new_basename = self.format_string(new_basename)
        new_file_path = join(self._destination, new_basename)
        if exists(new_file_path):
            logging.info('file exists: ' + new_file_path)
            return
        logging.info('new_file_path: ' + new_file_path)
        rename(self._source, new_file_path)

    ##################################################

    def format_string(self, string: str) -> str:
        if not isinstance(string, str):
            raise TypeError(f'{self.__class__.__name__}.string must be set to a string, {type(string)} given')
        if string == '':
            raise ValueError(f'{self.__class__.__name__}.string cannot be empty')
        # Remove accents from string (unicodedata method)
        string = ''.join(char for char in normalize('NFD', string) if category(char) != 'Mn')
        # Replace spaces with underscore and convert to lowercase
        return sub(' ', '_', string).lower()


##################################################

if __name__ == '__main__':
    pass
