#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Arbo Marekting POC package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from unittest import TestCase

from pyhelper.abstract_collection import AbstractCollection
from pyhelper.abstract_dto import AbstractDTO


class Dummy(AbstractDTO):
    def __init__(self, dictionary=None):
        self._id = None
        self._name = None
        self._email = None
        super().__init__(dictionary)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_):
        self._id = id_

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_):
        self._name = name_

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_):
        self._email = email_


class AbstractCollectionTest(TestCase):
    """
    AbstractCollectionTest
    """

    ITEMS = [
        {
            'id': 1,
            'name': 'tangoman',
            'email': 'mat@tangoman.io',
        },
        {
            'id': 2,
            'name': 'foobar',
            'email': 'foobar@example.com',
        }
    ]

    ##################################################

    def _load_collection_fixture(self):
        self.fixtures = []
        # populating fixtures
        for item in self.ITEMS:
            self.fixtures.append(Dummy(item))

    ##################################################

    def setUp(self):
        self._load_collection_fixture()
        self.collection = AbstractCollection(self.fixtures, 'name')

    ##################################################

    def test_constructor(self):
        """==> object_.__init__ should return expected list"""
        collection = AbstractCollection(self.fixtures, 'name')
        self.assertEqual(list(collection), self.fixtures)

    ##################################################

    def test_get(self):
        """==> object_.get should return expected item"""
        self.assertEqual(self.collection.get('tangoman'), self.fixtures[0])

    ##################################################

    def test_add(self):
        """==> object_.add should update collection"""
        self.collection.add(Dummy({'name': 'pingpong'}))
        self.assertEqual(len(self.collection), 3)
        for item in self.collection:
            self.assertTrue(item.name in ['tangoman', 'foobar', 'pingpong'])

    def test_add_no_duplicate(self):
        """==> object_.add should not create duplicates"""
        self.collection.add(Dummy(self.ITEMS[0]))
        self.assertEqual(len(self.collection), 2)
        for item in self.collection:
            self.assertTrue(item.name in ['tangoman', 'foobar'])

    ##################################################

    def test_remove(self):
        """==> object_.remove should update collection"""
        self.collection.remove(self.fixtures[1])
        self.assertEqual(len(self.collection), 1)
        for item in self.collection:
            self.assertTrue(item.name in ['tangoman'])

    ##################################################

    def test_update(self):
        """==> object_.update should update collection"""
        foobar = Dummy({'name': 'foobar', 'id': 666})
        self.collection.update(foobar)
        self.assertEqual(len(self.collection), 2)
        for item in self.collection:
            self.assertTrue(item.name in ['tangoman', 'foobar'])
        self.assertEqual(self.collection.get('foobar'), foobar)

    def test_update_no_overwrite(self):
        """==> object_.update should not overwrite empty values"""
        foobar = Dummy({'name': 'foobar', 'id': 666})
        expected = Dummy({'name': 'foobar', 'email': 'foobar@example.com', 'id': 666})
        self.collection.update(foobar)
        self.assertEqual(len(self.collection), 2)
        for item in self.collection:
            self.assertTrue(item.name in ['tangoman', 'foobar'])
        self.assertEqual(self.collection.get('foobar'), expected)

    ##################################################

    def test_iter(self):
        """==> object_.__iter__ should return expected value"""
        for item in self.collection:
            self.assertTrue(item.name in ['tangoman', 'foobar'])

    ##################################################

    def test_list(self):
        """==> list(object_) should return expected list"""
        self.assertEqual(list(self.collection), self.fixtures)

    ##################################################

    def test_len(self):
        """==> len(object_) should return item count"""
        self.assertEqual(len(self.collection), 2)
