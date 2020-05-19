#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from typing import Optional
from unittest import TestCase

from pyhelper.abstract_dto import AbstractDTO


class FooBar(AbstractDTO):
    def __init__(self, dictionary=None):
        self._foo = None
        self._bar = None
        super().__init__(dictionary)

    @property
    def foo(self) -> Optional[str]:
        return self._foo

    @foo.setter
    def foo(self, foo_: str) -> None:
        self._foo = foo_

    @property
    def bar(self) -> Optional[str]:
        return self._bar

    @bar.setter
    def bar(self, bar_: str) -> None:
        self._bar = bar_


class AbstractDTOTest(TestCase):
    """
    AbstractDTOTest
    """

    FIXTURES = {
        'bar': 'bar',
        'foo': 'foo'
    }

    STRING = '{"bar": "bar", "foo": "foo"}'

    ##################################################

    def setUp(self):
        self.dto = FooBar(self.FIXTURES)

    ##################################################
    # Test constructor
    ##################################################

    def test_constructor_setter(self):
        """==> Constructor should set expected values"""
        self.assertEqual(self.dto.foo, 'foo')
        self.assertEqual(self.dto.bar, 'bar')

    def test_constructor_attributeerror(self):
        """==> object_.__init__ should raise AttributeError"""
        with self.assertRaises(AttributeError):
            FooBar({'ping': 'pong'})

    def test_constructor_typeerror(self):
        """==> object_.__init__ should raise TypeError"""
        with self.assertRaises(TypeError):
            FooBar('invalid_type')

    def test_constructor_valueerror(self):
        """==> object_.__init__ should raise ValueError"""
        with self.assertRaises(ValueError):
            FooBar({})

    ##################################################
    # Test Properties
    ##################################################

    def test_properties(self):
        """==> object_.__properties__ should return expected list"""
        self.assertEqual(self.dto.__properties__, ['bar', 'foo'])

    ##################################################
    # Dunders / Built in Functions
    ##################################################

    def test_bool(self):
        """==> bool(object_) should return expected boolean"""
        self.assertTrue(bool(self.dto))

    ##################################################

    def test_dict(self):
        """==> dict(object_) should return expected dictionary"""
        self.assertEqual(dict(self.dto), self.FIXTURES)

    ##################################################

    def test_eq(self):
        """==> object_ == object_ should return expected boolean"""
        self.assertEqual(self.dto, FooBar(self.FIXTURES))
        self.assertTrue(self.dto == FooBar(self.FIXTURES))
        self.assertFalse(self.dto == FooBar({'foo': 'pong'}))

    ##################################################

    def test_hash(self):
        """==> hash(object_) should return expected hash"""
        self.assertIsInstance(hash(self.dto), int)
        self.assertEqual(hash(self.dto), hash(FooBar(self.FIXTURES)))
        self.assertFalse(hash(self.dto) == hash(FooBar({'foo': 'pong'})))

    ##################################################

    def test_iter(self):
        """==> iteration over object_ should return expected values"""
        temp = [('bar', 'bar'), ('foo', 'foo')]
        i = 0
        for property_ in self.dto:
            self.assertEqual(property_, temp[i])
            i += 1

    ##################################################

    def test_len(self):
        """==> len(object_) should return expected integer"""
        self.assertIsInstance(len(self.dto), int)
        self.assertEqual(len(self.dto), len(self.FIXTURES))

    ##################################################

    def test_str(self):
        """==> str(object_) should return expected value"""
        self.assertIsInstance(str(self.dto), str)
        self.assertEqual(str(self.dto), self.STRING)
