#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from os import listdir
from os.path import join, exists, abspath
from typing import Optional, Iterable


class FolderManager:
    """
    FolderManager
    """

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, folder: str = None, extension: str = None):
        """Set folder when given folder path"""
        self._folder = None
        self._files = None
        self._extension = None
        if folder is not None:
            self.folder = folder
        if extension is not None:
            self.extension = extension

    ##################################################
    # folder Setter / Getter
    ##################################################

    @property
    def folder(self) -> Optional[str]:
        return self._folder

    @folder.setter
    def folder(self, folder: Optional[str]) -> None:
        if not isinstance(folder, str):
            raise TypeError(f'{self.__class__.__name__}.folder must be set to str, {type(folder)} given')
        if folder == '':
            raise ValueError(f'{self.__class__.__name__}.folder cannot be empty')
        path = abspath(folder)
        if not exists(path):
            raise OSError(f"{self.__class__.__name__}.folder not found")
        self._folder = path

    ##################################################
    # extension Setter / Getter
    ##################################################

    @property
    def extension(self) -> Optional[str]:
        return self._extension

    @extension.setter
    def extension(self, extension_: str) -> None:
        if not isinstance(extension_, str):
            raise TypeError(f'{self.__class__.__name__}.extension must be set to str, {type(extension_)} given')
        if extension_ == '':
            raise ValueError(f'{self.__class__.__name__}.extension cannot be empty, {type(extension_)} given')
        self._extension = extension_

    ##################################################
    # files Setter / Getter
    ##################################################

    def files(self, extension: str = None) -> Optional[list]:
        """List full file paths contained in folder filtered by extension (optional)"""
        if self._folder is None:
            raise ValueError(f"{self.__class__.__name__}.folder not found")
        if extension is not None:
            self.extension = extension
        if self.extension:
            return [join(self._folder, file) for file in listdir(self._folder) if file.endswith(self.extension)]
        else:
            return [join(self._folder, file) for file in listdir(self._folder)]

    ##################################################

    def __iter__(self) -> Iterable:
        """Iterate through files"""
        for file in self.files():
            yield file

    ##################################################

    def __len__(self) -> int:
        """Return file count"""
        return len(self.files())


##################################################

if __name__ == '__main__':
    pass
