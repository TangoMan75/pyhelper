#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from os.path import dirname
from unittest import TestCase

from pyhelper import Renamer


class RenamerTest(TestCase):
    """
    RenamerTest
    """

    ##################################################

    def setUp(self):
        self.renamer = Renamer(dirname(__file__) + '/fixtures/foobar.txt')

    ##################################################

    def test_renamer_format_string_typeerror(self):
        """==> renamer.format_string should raise TypeError"""
        with self.assertRaises(TypeError):
            self.renamer.format_string(b'')

    def test_renamer_format_string_valueerror(self):
        """==> renamer.format_string should raise ValueError"""
        with self.assertRaises(ValueError):
            self.renamer.format_string('')

    def test_renamer_format_string(self):
        """==> renamer.format_string should return expected str"""
        self.assertIsInstance(self.renamer.format_string('foobar'), str)
        self.assertEqual(self.renamer.format_string('fÔô Bâr'), 'foo_bar')

    ##################################################

    def test_renamer_source_typeerror(self):
        """==> renamer.source should raise TypeError"""
        with self.assertRaises(TypeError):
            self.renamer.source = b''

    def test_renamer_source_valueerror(self):
        """==> renamer.source should raise ValueError"""
        with self.assertRaises(ValueError):
            self.renamer.source = ''

    def test_renamer_source_should_update_destination(self):
        """==> renamer.source should update destination"""
        self.assertIsInstance(self.renamer.destination, str)
        self.assertEqual(self.renamer.destination, dirname(__file__) + '/fixtures')

    ##################################################

    def test_renamer_destination_typeerror(self):
        """==> renamer.destination should raise TypeError"""
        with self.assertRaises(TypeError):
            self.renamer.destination = b''

    def test_renamer_destination_valueerror(self):
        """==> renamer.destination should raise ValueError"""
        with self.assertRaises(ValueError):
            self.renamer.destination = ''
