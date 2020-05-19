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

from pyhelper.serializer import Serializer


class FooBar():
    def __init__(self, dictionary=None):
        self._foo = None
        self._bar = None

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


class SerializerTest(TestCase):
    """
    SerializerTest
    """

    FIXTURES = {
        'bar': 'bar',
        'foo': 'foo'
    }

    STRING = '{"bar": "bar", "foo": "foo"}'

    ##################################################

    def setUp(self):
        foobar = FooBar()
        foobar.foo = 'foo'
        foobar.bar = 'bar'
        self.serializer = Serializer(foobar)

    ##################################################
    # Test Encoder
    ##################################################

    def test_encode_typeerror(self):
        """==> object_.encode should raise TypeError"""
        with self.assertRaises(TypeError):
            self.serializer.encode('invalid_value')

    def test_encode_valueerror(self):
        """==> object_.encode should raise ValueError"""
        with self.assertRaises(ValueError):
            self.serializer.encode({})

    def test_encode(self):
        """==> object_.encode should return expected value"""
        self.assertEqual(self.serializer.encode(self.FIXTURES), self.STRING)

    # ##################################################
    # Test Decoder
    ##################################################

    def test_decode_typeerror(self):
        """==> object_.decode should raise TypeError"""
        with self.assertRaises(TypeError):
            self.serializer.decode({'invalid_value': False})

    def test_decode_valueerror(self):
        """==> object_.decode should raise ValueError"""
        with self.assertRaises(ValueError):
            self.serializer.decode('')

    def test_decode(self):
        """==> object_.decode should return expected value"""
        self.assertEqual(self.serializer.decode(self.STRING), self.FIXTURES)

    ##################################################
    # Test serialize
    ##################################################

    def test_serialize(self):
        """==> object_.serialize should return expected value"""
        self.assertEqual(self.serializer.serialize(), self.STRING)

    ##################################################
    # Test Deserializer
    ##################################################

    def test_deserialize_typeerror(self):
        """==> object_.deserialize should raise TypeError"""
        with self.assertRaises(TypeError):
            self.serializer.deserialize({'invalid_value': False})

    def test_deserialize_valueerror(self):
        """==> object_.deserialize should raise ValueError"""
        with self.assertRaises(ValueError):
            self.serializer.deserialize('')

    def test_deserialize(self):
        """==> object_.deserialize should return expected value"""
        self.assertIsInstance(self.serializer.deserialize(self.STRING), FooBar)

    ##################################################
    # Test Normalizer
    ##################################################

    def test_normalize(self):
        """==> object_.normalize should return expected value"""
        self.assertEqual(self.serializer.normalize(), self.FIXTURES)

    ##################################################
    # Test Denormalizer
    ##################################################

    def test_denormalizer_attributeerror(self):
        """==> object_.denormalize should raise AttributeError"""
        with self.assertRaises(AttributeError):
            self.serializer.denormalize({'ping': 'pong'})

    def test_denormalizer_typeerror(self):
        """==> object_.denormalize should raise TypeError"""
        with self.assertRaises(TypeError):
            self.serializer.denormalize('invalid_type')

    def test_denormalizer_valueerror(self):
        """==> object_.denormalize should raise ValueError"""
        with self.assertRaises(ValueError):
            self.serializer.denormalize({})
