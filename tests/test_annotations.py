#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyAnnotations package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from typing import Optional, Union
from unittest import TestCase

from pyhelper.annotations import Annotations


##################################################

class FooBar:

    def __init__(self):
        self._id = None

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, id_: Union[int, type(None)]) -> None:
        self._id = id_

    def foobar(self, string: str = 'foobar') -> Optional[str]:
        return string


##################################################


class TestAnnotations(TestCase):

    def setUp(self):
        self.foobar = FooBar()
        self.annotations = Annotations(self.foobar)

    ##################################################

    def test_get_properties(self):
        self.assertIsInstance(self.annotations.get_properties, list)
        self.assertEqual(self.annotations.get_properties, ['id'])

    ##################################################

    def test_get_methods(self):
        self.assertIsInstance(self.annotations.get_methods, list)
        self.assertEqual(self.annotations.get_methods, ['foobar'])

    ##################################################

    def test_get_static(self):
        self.assertIsInstance(self.annotations.get_static, dict)
        static = self.annotations.get_static
        for member in static.keys():
            self.assertTrue(member in ['id', 'foobar'])
        self.assertIsInstance(static.get('id'), property)
        self.assertTrue(callable(static.get('foobar')))

    ##################################################

    def test_get_annotations(self):
        self.assertIsInstance(self.annotations.get_annotations, dict)
        self.assertEqual(self.annotations.get_annotations,
                         {'id': {
                             'fget': {'return': Union[int, None]},
                             'fset': {'id_': Union[int, None], 'return': None}
                         },
                             'foobar': {'string': str, 'return': Union[str, None]}
                         })
