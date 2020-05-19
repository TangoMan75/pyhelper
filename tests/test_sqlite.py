#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from sqlite3 import IntegrityError
from sqlite3 import OperationalError
from unittest import TestCase

from pyhelper import Sqlite


class SqliteTest(TestCase):
    """
    SqliteTest
    """

    DUMMY_SCHEMA = {
        'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE',
        'foo': 'TEXT',
        'bar': 'TEXT'
    }

    MOCK_SCHEMA = {
        'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE',
        'email': 'TEXT NOT NULL'
    }

    ##################################################

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
        self.db = Sqlite()
        self.db.create('users', self.MOCK_SCHEMA)

    ##################################################

    def test_create(self):
        """==> Create table should not raise error"""
        try:
            self.db.create('foobar', self.DUMMY_SCHEMA)
        except Exception as e:
            self.fail(e)

    ##################################################

    def test_insert(self):
        """==> Insert return last inserted id"""
        lastrowid = self.db.insert('users', {'id': None, 'email': 'foobar@example.com'})
        self.assertEqual(lastrowid, 1)

    ##################################################

    def test_find(self):
        """==> Find returns correct item"""
        lastrowid = self.db.insert('users', {'id': None, 'email': 'foobar@example.com'})
        item = self.db.find('users', {'id': 1})
        self.assertEqual(item, [(1, 'foobar@example.com')])

    ##################################################

    def test_find_nonexistant(self):
        """==> Invalid id returns empty list"""
        item = self.db.find('users', {'id': 666})
        self.assertEqual(item, [])

    ##################################################

    def test_insert_into_multiple_tables(self):
        """==> Insert data into multiple tables"""
        self.db.create('foobar', self.DUMMY_SCHEMA)

        # Insert returns correct lastrowid
        lastrowid = self.db.insert('users', {'id': 666, 'email': 'foobar@example.com'})
        self.assertEqual(lastrowid, 666)
        item = self.db.find('users', {'id': 666})
        self.assertEqual(item, [(666, 'foobar@example.com')])

        lastrowid = self.db.insert('foobar', {'id': None, 'foo': 'foo', 'bar': 'bar'})
        self.assertEqual(lastrowid, 1)
        item = self.db.find('foobar', {'id': 1})
        self.assertEqual(item, [(1, 'foo', 'bar')])

    ##################################################

    def test_delete(self):
        """==> Test delete item"""
        lastrowid = self.db.insert('users', {'id': 69, 'email': 'foobar@example.com'})
        self.assertEqual(lastrowid, 69)

        self.db.delete('users', {'id': lastrowid})
        item = self.db.find('users', {'id': 69})
        self.assertEqual(item, [])

    ##################################################

    def test_delete_nonexistant(self):
        """==> delete nonexistent doesnot raise error"""
        self.db.delete('users', {'id': 666})

    ##################################################

    def test_sanitize(self):
        """==> sanitize method returns expected string"""
        self.assertEqual(self.db.sanitize('!"#$%\'()*+,-/:;=@[\\]`{|}~'), '')

    ##################################################
    # TypeError / ValueError
    ##################################################

    def test_typeerror_create_schema_string(self):
        """==> create table must be set to None or a string"""
        for value in self.TEST_NULLABLE_STRING:
            with self.assertRaises(TypeError):
                self.db.create(value, 'table')

    def test_valueerror_insert_empty_data(self):
        """==> insert data cannot be empty"""
        with self.assertRaises(ValueError):
            self.db.insert('users', {})

    ##################################################

    def test_typeerror_insert_table_string(self):
        """==> insert table must be set to a string"""
        item = {'id': None, 'email': 'foobar@example.com'}
        for value in self.TEST_NULLABLE_STRING:
            with self.assertRaises(TypeError):
                self.db.insert(value, item)

    def test_typeerror_insert_table_dict(self):
        """==> insert table must be set to a dictionary"""
        for value in self.TEST_DICTIONARY:
            with self.assertRaises(TypeError):
                self.db.insert('users', value)

    ##################################################

    def test_valueerror_find_empty_data(self):
        """==> find data cannot be empty"""
        with self.assertRaises(ValueError):
            self.db.find('users', {})

    def test_typeerror_find_table_string(self):
        """==> find table must be set to a string"""
        item = {'id': None, 'email': 'foobar@example.com'}
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.db.find(value, item)

    def test_typeerror_find_table_dict(self):
        """==> find table must be set to a dictionary"""
        for value in self.TEST_DICTIONARY:
            with self.assertRaises(TypeError):
                self.db.find('users', value)

    ##################################################

    def test_valueerror_delete_empty_data(self):
        """==> delete data cannot be empty"""
        with self.assertRaises(ValueError):
            self.db.delete('users', {})

    def test_typeerror_delete_table_string(self):
        """==> delete table must be set to a string"""
        item = {'id': None, 'email': 'foobar@example.com'}
        for value in self.TEST_STRING:
            with self.assertRaises(TypeError):
                self.db.delete(value, item)

    def test_typeerror_delete_table_dict(self):
        """==> delete table must be set to a dictionary"""
        for value in self.TEST_DICTIONARY:
            with self.assertRaises(TypeError):
                self.db.delete('users', value)

    ##################################################

    def test_integrityerror_insert_twice(self):
        """==> Insert twice returns integrityerror: unique constraint failed"""
        self.db.insert('users', {'id': 1, 'email': 'foobar@example.com'})
        with self.assertRaises(IntegrityError):
            self.db.insert('users', {'id': 1, 'email': 'foobar@example.com'})

    ##################################################

    def test_operationalerror_create_twice(self):
        """==> Create same table twice raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.create('users', self.MOCK_SCHEMA)

    ##################################################

    def test_operationalerror_insert_invalid_column(self):
        """==> Invalid column raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.insert('users', {'foo': 'bar'})

    def test_operationalerror_insert_invalid_table(self):
        """==> Invalid table raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.insert('foobar', {'foo': 'bar'})

    ##################################################

    def test_operationalerror_find_invalid_column(self):
        """==> Invalid column raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.find('users', {'foo': 'bar'})

    def test_operationalerror_find_invalid_table(self):
        """==> Invalid table raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.find('foobar', {'foo': 'bar'})

    ##################################################

    def test_operationalerror_delete_invalid_column(self):
        """==> Invalid column raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.delete('users', {'foo': 'bar'})

    def test_operationalerror_delete_invalid_table(self):
        """==> Invalid table raises OperationalError exception"""
        with self.assertRaises(OperationalError):
            self.db.delete('foobar', {'foo': 'bar'})

    ##################################################

    def tearDown(self):
        self.db.close()
