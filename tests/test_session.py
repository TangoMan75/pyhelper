#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyhelper import Session


class SessionTest(TestCase):
    """
    SessionTest
    """

    # fixtures for "_test_typeerror" method
    BOOLEANS = (True, False)
    DICTIONARIES = ({'dictionary': True}, {})
    FLOATS = (-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, -3.1, -2.1, -1.1, 0.1, 1.1, 2.1, 3.1)
    INTEGERS = (-3, -2, -1, 0, 1, 2, 3)
    LISTS = (['list'], [])
    NULL = (None,)
    STRINGS = ('string', '')

    TEST_BOOLEAN = DICTIONARIES + FLOATS + INTEGERS + LISTS + NULL + STRINGS
    TEST_NULLABLE_BOOLEAN = DICTIONARIES + FLOATS + INTEGERS + LISTS + STRINGS

    TEST_DICTIONARY = BOOLEANS + FLOATS + INTEGERS + LISTS + NULL + STRINGS
    TEST_NULLABLE_DICTIONARY = BOOLEANS + FLOATS + INTEGERS + LISTS + STRINGS

    TEST_FLOAT = BOOLEANS + DICTIONARIES + INTEGERS + LISTS + NULL + STRINGS
    TEST_NULLABLE_FLOAT = BOOLEANS + DICTIONARIES + INTEGERS + LISTS + STRINGS

    TEST_INTEGER = BOOLEANS + DICTIONARIES + FLOATS + LISTS + NULL + STRINGS
    TEST_NULLABLE_INTEGER = BOOLEANS + DICTIONARIES + FLOATS + LISTS + STRINGS

    TEST_LIST = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + NULL + STRINGS
    TEST_NULLABLE_LIST = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + STRINGS

    TEST_STRING = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + LISTS + NULL
    TEST_NULLABLE_STRING = BOOLEANS + DICTIONARIES + FLOATS + INTEGERS + LISTS

    ##################################################

    def setUp(self):
        self.session = Session()

    ##################################################

    def test_init(self):
        """==> tor must be set to a boolean"""
        for value in self.TEST_BOOLEAN:
            with self.assertRaises(TypeError):
                self.session = Session(value)

    ##################################################

    def test_get_random_user_agent(self):
        """==> get_random_user_agent returns string"""
        self.assertIsInstance(self.session.get_random_user_agent(), str)

    ##################################################

    def test_raise_typeerror_send_request_url_string(self):
        """==> uri must be set to a string"""
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.session.send_request(value)

    def test_raise_valueerror_send_request_uri_string(self):
        """==> uri cannot be empty"""
        with self.assertRaises(ValueError):
            self.session.send_request('')

    ##################################################

    def test_raise_typeerror_send_request_user_agents_list(self):
        """==> user_agents must be set to a list"""
        for value in self.TEST_LIST:
            with self.assertRaises(TypeError):
                self.session.send_request('string', value)

    def test_send_request_with_empty_user_agents_list(self):
        """==> send_request without user_agents list should not raise error"""
        try:
            self.session.send_request('string', [])
        except Exception as e:
            self.fail(e)

    ##################################################

    def test_raise_typeerror_send_request_timeout_integer(self):
        """==> timeout must be set to None or an integer"""
        for value in self.TEST_NULLABLE_INTEGER:
            with self.assertRaises(TypeError):
                self.session.send_request('string', timeout=value)

    def test_raise_valueerror_send_request_timeout_positive_integer(self):
        """==> timeout must be positive integer"""
        with self.assertRaises(ValueError):
            self.session.send_request('string', timeout=-1)

    ##################################################

    def test_raise_typeerror_send_request_allow_redirects_boolean(self):
        """==> allow_redirects must be set to a boolean"""
        for value in self.TEST_BOOLEAN:
            with self.assertRaises(TypeError):
                self.session.send_request('string', allow_redirects=value)
