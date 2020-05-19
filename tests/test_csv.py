#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyhelper import CSV


class CSVTest(TestCase):
    """
    CSVTest
    """

    # fixtures for "_test_typeerror" method
    BOOLEANS = (True, False)
    DICTIONARIES = ({'dictionary': True}, {})
    FLOATS = (-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, -3.1, -2.1, -1.1, 0.1, 1.1, 2.1, 3.1)
    INTEGERS = (-3, -2, -1, 0, 1, 2, 3)
    LISTS = (['list'], [])
    NULL = (None,)
    STRINGS = ('string', '')

    TEST_LIST = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + NULL + STRINGS
    TEST_STRING = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + LISTS + NULL

    ##################################################

    def setUp(self):
        self.csv = CSV()

    ##################################################

    def test_typeerror_read_file_path_string(self):
        """==> file_path must be set to a string"""
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.csv.read(value)

    ##################################################

    def test_oserror_read_file_path_exists(self):
        """==> file_path must be set to an existing path"""
        with self.assertRaises(OSError):
            self.csv.read('non_existant.csv')

    ##################################################

    def test_valueerror_write_empty_data(self):
        """==> data cannot be empty"""
        with self.assertRaises(ValueError):
            self.csv.write([], 'foobar.csv')

    def test_typeerror_write_list_dictionaries(self):
        """==> data must contain a list of dictionaries"""
        with self.assertRaises(TypeError):
            self.csv.write(['foobar'], 'foobar.csv')

    def test_valueerror_write_empty_dictionary(self):
        """==> data cannot contain empty dictionaries"""
        with self.assertRaises(ValueError):
            self.csv.write([{}], 'foobar.csv')

    ##################################################

    def test_typeerror_write_data_list(self):
        """==> data must be set to a list"""
        for value in self.TEST_LIST:
            with self.assertRaises(TypeError):
                self.csv.write(value, 'foobar.csv')

    def test_typeerror_write_file_path_string(self):
        """==> file_path must be set to a string"""
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.csv.write([{"foo": "bar"}], value)
