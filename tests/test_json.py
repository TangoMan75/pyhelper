#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyhelper import Json


class JsonTest(TestCase):
    """
    JsonTest
    """

    # fixtures for "_test_typeerror" method
    BOOLEANS = (True, False)
    DICTIONARIES = ({'dictionary': True}, {})
    FLOATS = (-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, -3.1, -2.1, -1.1, 0.1, 1.1, 2.1, 3.1)
    INTEGERS = (-3, -2, -1, 0, 1, 2, 3)
    LISTS = (['list'], [])
    NULL = (None,)
    STRINGS = ('string', '')

    TEST_STRING = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + LISTS + NULL
    TEST_LIST_DICTIONARY = BOOLEANS + FLOATS + INTEGERS + NULL + STRINGS

    ##################################################

    def setUp(self):
        self.json = Json()

    ##################################################

    def test_typeerror_read_file_path_string(self):
        """==> file_path must be set to a string"""
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.json.read(value)

    ##################################################

    def test_oserror_read_file_path_exists(self):
        """==> file_path must be set to an existing path"""
        with self.assertRaises(OSError):
            self.json.read('non_existant.json')

    ##################################################

    def test_typeerror_write_data_list_dictionary(self):
        """==> data must be set to a list or a dictionary"""
        for value in self.TEST_LIST_DICTIONARY:
            with self.assertRaises(TypeError):
                self.json.write(value)

    def test_typeerror_write_file_path_string(self):
        """==> file_path must be set to a string"""
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.json.write([{"foo": "bar"}], value)
