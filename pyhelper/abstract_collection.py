#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from typing import Any


class AbstractCollection:
    """
    AbstractCollection

    Manage item collection with a unique field as index.

    - add: Append item to collection or update existing item
    - update: Merge values from current item with updated values when not empty

    Constructor
    -----------
    - __init__: Build collection from list and set index
    NOTE: Remember to pass on "dictionary" parameter with "super()" syntax when required
    ```
    def __init__(self, items: list = None) -> None:
        super().__init__(items, 'unique_field')
    ```

    Dunders
    -------
    - __iter__: Allow object iteration, dict(self) and list(self) methods
    - __len__:  Return property count
    """

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, items: list = None, index: str = None) -> None:
        """Build collection from list and set index"""
        if not isinstance(items, list):
            raise TypeError(f'{self.__class__.__name__} items must be set to list, {type(items)} given')
        if not isinstance(index, str):
            raise TypeError(f'{self.__class__.__name__} index must be set to str, {type(index)} given')
        self._index = index
        self._items = {}
        for item in items:
            self.add(item)

    ##################################################
    # collection methods
    ##################################################

    def get(self, index: str) -> Any:
        """Return item by index"""
        try:
            return self._items[index]
        except KeyError:
            raise KeyError(f'{self.__class__.__name__}.get "{index}" not found')

    ##################################################

    def add(self, item: Any) -> None:
        """Append item to collection or update existing item"""
        try:
            index_ = item.__getattribute__(self._index)
        except KeyError:
            raise KeyError(f'{item.__class__.__name__} has no attribute "{self._index}"')
        if self._items.get(index_) is None:
            self._items[index_] = item
        else:
            self.update(item)

    ##################################################

    def remove(self, item: Any) -> None:
        """Remove item from collection"""
        try:
            index_ = item.__getattribute__(self._index)
        except KeyError:
            raise KeyError(f'{item.__class__.__name__} has no attribute "{self._index}"')
        try:
            del (self._items[index_])
        except KeyError:
            raise KeyError(f'{self.__class__.__name__}.remove "{index_}" not found')

    ##################################################

    def update(self, item: Any) -> None:
        """Merge values from current item with updated values when not empty"""
        try:
            index_ = item.__getattribute__(self._index)
        except KeyError:
            raise KeyError(f'{item.__class__.__name__} has no attribute "{self._index}"')
        # find current item
        current_item = self._items[index_]
        # when current item is different from new one
        if current_item != item:
            # Updating empty values if any
            for key, value in item:
                if value is None:
                    item.__setattr__(key, current_item.__getattribute__(key))
            self._items[index_] = item

    ##################################################

    def __iter__(self) -> Any:
        """Allow object iteration"""
        for item in self._items.values():
            yield item

    ##################################################

    def __len__(self) -> int:
        """Return item count"""
        return len(self._items)


##################################################


if __name__ == '__main__':
    pass
