#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from os.path import dirname, isfile
from unittest import TestCase

from pyhelper import FolderManager


class FolderManagerTest(TestCase):
    """
    FolderManagerTest
    """

    ##################################################

    def setUp(self):
        self.folder_manager = FolderManager(dirname(__file__) + '/fixtures')

    ##################################################

    def test_folder_setter_typeerror(self):
        """==> object_.folder should raise TypeError"""
        with self.assertRaises(TypeError):
            self.folder_manager.folder = b''

    def test_folder_setter_valueerror(self):
        """==> object_.folder should raise ValueError"""
        with self.assertRaises(ValueError):
            self.folder_manager.folder = ''

    def test_folder_setter_folder_doesnt_exist_os_error(self):
        """==> Missing folder should raise OSError"""
        with self.assertRaises(OSError):
            self.folder_manager.folder = './not_a_folder'

    def test_folder_getter(self):
        """==> object_.folder should return expected string"""
        self.assertEqual(self.folder_manager.folder, dirname(__file__) + '/fixtures')

    ##################################################

    def test_extension_setter_typeerror(self):
        """==> object_.extension should raise TypeError"""
        with self.assertRaises(TypeError):
            self.folder_manager.extension = b''

    def test_extension_setter_valueerror(self):
        """==> object_.extension should raise ValueError"""
        with self.assertRaises(ValueError):
            self.folder_manager.extension = ''

    ##################################################

    def test_files_getter_valueerror(self):
        """==> Empty object_.files should raise ValueError"""
        self.folder_manager = FolderManager()
        with self.assertRaises(ValueError):
            self.folder_manager.files()

    def test_files_getter(self):
        """==> object_.files should return expected list"""
        for file in self.folder_manager.files():
            self.assertTrue(isfile(file))

    def test_files_getter_with_filter(self):
        """==> object_.files should return expected list"""
        for file in self.folder_manager.files('.md'):
            self.assertTrue(file.endswith('.md'))

    ##################################################

    def test_folder_manager_count(self):
        """==> len(object_) should return expected count"""
        self.assertEqual(len(self.folder_manager), 4)

    ##################################################

    def test_folder_manager_iterator(self):
        """==> object_ should return expected values"""
        for file in self.folder_manager:
            self.assertTrue(isfile(file))

    def test_folder_manager_iterator_with_filter(self):
        """==> object_ should return expected values"""
        self.folder_manager.extension = '.md'
        for file in self.folder_manager:
            self.assertTrue(file.endswith('.md'))
