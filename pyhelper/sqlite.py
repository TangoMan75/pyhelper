#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from sqlite3 import (connect, OperationalError)


class Sqlite:
    """
    Read/write from/to sqlite database.
    https://www.sqlite.org/datatype3.html
    """

    DATATYPES = (
        'BLOB',
        'INTEGER',
        'REAL',
        'TEXT'
    )

    ATTRIBUTES = (
        'AUTOINCREMENT',
        'NOT NULL',
        'PRIMARY KEY',
        'UNIQUE'
    )

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, db_file: str = ':memory:', autocommit: bool = True, journal_mode: str = 'off'):
        """
        create_connection
        https://sqlite.org/pragma.html
        """
        if not isinstance(db_file, str):
            raise TypeError('db_file must be set to a string')
        if not isinstance(autocommit, bool):
            raise TypeError('autocommit must be set to a boolean')
        if not isinstance(journal_mode, str):
            raise TypeError('journal_mode must be set to a string')
        if not db_file:
            raise ValueError('db_file cannot be empty')
        self.connection = None
        self.cursor = None
        try:
            if autocommit:
                # open database in autocommit mode by setting isolation_level to none
                self.connection = connect(db_file, isolation_level=None)
            else:
                self.connection = connect(db_file)
            # disable rollback journal (heavy disk usage)
            self.connection.execute('pragma journal_mode=' + journal_mode)
            self.cursor = self.connection.cursor()
        except OperationalError as e:
            raise e

    ##################################################

    def create(self, table: str, schema: dict):
        """
        create
        """
        if not isinstance(table, str):
            raise TypeError('table must be set to a string')
        if not isinstance(schema, dict):
            raise TypeError('schema must be set to a dictionary')
        if len(schema) == 0:
            raise ValueError('schema cannot be empty')
        table = self.sanitize(table)
        sql = 'CREATE TABLE "' + table + '" (' + ', '.join(list(map(
            lambda key, datatype: '"' + self.sanitize(key) + '" ' + datatype, schema.keys(), schema.values()
        ))) + ');'
        try:
            self.cursor.execute(sql)
        except OperationalError as e:
            raise e
        else:
            return self.cursor.lastrowid

    ##################################################

    def insert(self, table: str, item: dict):
        """
        insert
        """
        if not isinstance(table, str):
            raise TypeError('table must be set to a string')
        if not isinstance(item, dict):
            raise TypeError('item must be set to a dictionary')
        if len(item) == 0:
            raise ValueError('item cannot be empty')
        table = self.sanitize(table)
        # lambda: prefix colon to each key
        sql = 'INSERT INTO "' + table + '" VALUES(' + ', '.join(list(map(
            lambda key: ':' + self.sanitize(key), item.keys()
        ))) + ');'
        try:
            self.cursor.execute(sql, item)
        except OperationalError as e:
            raise e
        else:
            return self.cursor.lastrowid

    ##################################################

    def find(self, table: str, item: dict) -> list:
        """
        find
        """
        if not isinstance(table, str):
            raise TypeError('table must be set to a string')
        if not isinstance(item, dict):
            raise TypeError('item must be set to a dictionary')
        if len(item) == 0:
            raise ValueError('item cannot be empty')
        table = self.sanitize(table)
        key = self.sanitize(str(list(item.keys())[0]))
        value = str(list(item.values())[0])
        sql = 'SELECT * FROM "' + table + '" WHERE ' + key + '=:' + key
        self.cursor.execute(sql, {key: value})
        return self.cursor.fetchall()

    ##################################################

    def delete(self, table: str, item: dict) -> None:
        """
        delete
        """
        if not isinstance(table, str):
            raise TypeError('table must be set to a string')
        if not isinstance(item, dict):
            raise TypeError('item must be set to a dictionary')
        if len(item) == 0:
            raise ValueError('item cannot be empty')
        table = self.sanitize(table)
        key = self.sanitize(str(list(item.keys())[0]))
        value = str(list(item.values())[0])
        sql = 'DELETE FROM "' + table + '" WHERE ' + key + '=:' + key
        self.cursor.execute(sql, {key: value})

    ##################################################

    def commit(self) -> None:
        """
        commit
        """
        self.connection.commit()

    ##################################################

    def close(self) -> None:
        """
        close
        """
        self.connection.close()

    ##################################################

    @staticmethod
    def sanitize(string: str) -> str:
        """
        sanitize
        """
        return ''.join([char for char in string if char.isalnum()])


##################################################


if __name__ == '__main__':
    pass
