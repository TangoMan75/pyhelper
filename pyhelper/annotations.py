#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyAnnotations package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled

 with this source code in the file LICENSE.
"""

from platform import python_version
from typing import Any

if python_version()[0:3] < '3.7':
    print('\033[93m[!] Make sure you have Python 3.7+ installed, quitting.\n\n \033[0m')
    exit(1)


class Annotations:
    """
    Return annotations from given object

    - get_properties:  Return object public properties
    - get_methods:     Return object public and protected methods name
    - get_static:      Return all class members statically
    - get_annotations: Return class members annotations
    """

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, object_: Any) -> None:
        self._object = object_

    ##################################################
    # Get Properties
    ##################################################

    @property
    def get_properties(self) -> list:
        """Return object public properties name"""
        return [name for name in dir(self._object) if
                not name.startswith('_') and not callable(self._object.__getattribute__(name))]

    ##################################################
    # Get Methods
    ##################################################

    @property
    def get_methods(self) -> list:
        """Return object public and protected methods name"""
        return [name for name in dir(self._object) if
                not name.startswith('__') and callable(self._object.__getattribute__(name))]

    ##################################################
    # Get Static
    ##################################################

    @property
    def get_static(self) -> dict:
        """Return object members statically"""
        members = {}
        for property_ in self.get_properties:
            members[property_] = type.__getattribute__(type(self._object), property_)
        for method_ in self.get_methods:
            members[method_] = type.__getattribute__(type(self._object), method_)
        return members

    ##################################################
    # Get Annotations
    ##################################################

    @property
    def get_annotations(self) -> dict:
        """Return object members annotations"""
        annotations = {}
        for property_ in self.get_properties:
            annotations[property_] = {
                'fget': type.__getattribute__(type(self._object), property_).fget.__annotations__,
                'fset': type.__getattribute__(type(self._object), property_).fset.__annotations__,
            }
        for method_ in self.get_methods:
            annotations[method_] = type.__getattribute__(type(self._object), method_).__annotations__
        return annotations


##################################################


if __name__ == '__main__':
    pass
