#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from json import (dumps)
from typing import Any


class AbstractDTO:
    """
    Abstract DTO
    ======

    Extend your model with this class to access following useful features:

    Dunders
    -------
    - __bool__: Return False when object has empty property
    - __eq__:   Implement equal operator
    - __hash__: Implement hash(self) method
    - __iter__: Allow object iteration, dict(self) and list(self) methods
    - __len__:  Return property count
    - __repr__: Return object as json string

    Special attribute
    -----------------
    - __properties__: Return object public properties

    Constructor
    -----------
    - __init__: Hydrate object when given dictionary
    NOTE: Remember to pass on "dictionary" parameter with "super()" syntax when required
    ```
    def __init__(self, dictionary: dict = None) -> None:
        self._foo = None
        self._bar = None
        super().__init__(dictionary)
    ```
    """

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, dictionary: dict = None) -> None:
        """Hydrate object when given dictionary"""
        if dictionary is not None:
            if not isinstance(dictionary, dict):
                raise TypeError(f'{self.__class__.__name__}.__init__: must be set to a dictionary')
            if dictionary == {}:
                raise ValueError(f'{self.__class__.__name__}.__init__: dictionary cannot be empty')
            # dictionary keys must match object properties
            for property_ in dictionary.keys():
                if property_ not in self.__properties__:
                    raise AttributeError(f'{self.__class__.__name__} has no attribute {property_}')
            # setting given attributes from dictionary (using appropriate setters)
            for key_, value_ in dictionary.items():
                setattr(self, key_, value_)

    ##################################################
    # Properties
    ##################################################

    @property
    def __properties__(self) -> list:
        """Return object public properties name"""
        return [name for name in dir(self) if not name.startswith('_') and not callable(self.__getattribute__(name))]

    ##################################################
    # Dunders / Built in Functions
    ##################################################

    def __bool__(self) -> bool:
        """Return False when object has empty property
        https://docs.python.org/3/reference/datamodel.html#object.__bool__
        NOTE: cannot use "self.getattr()" from extended class; using "__getattribute__" instead:
        https://docs.python.org/3/reference/datamodel.html#object.__getattribute__
        """
        for property_ in self.__properties__:
            if self.__getattribute__(property_) is None:
                return False
        return True

    ##################################################

    def __eq__(self, other: Any) -> bool:
        """Implement equal operator
        https://docs.python.org/3/reference/datamodel.html#object.__eq__
        """
        if not isinstance(other, type(self)):
            return False
        for property_ in self.__properties__:
            if self.__getattribute__(property_) != other.__getattribute__(property_):
                return False
        return True

    ##################################################

    def __hash__(self) -> int:
        """Return object hash
        https://docs.python.org/3/reference/datamodel.html#object.__hash__
        """
        return hash(tuple(dict(self).values()))

    ##################################################

    def __iter__(self) -> Any:
        """Allow object iteration
        https://docs.python.org/3/reference/datamodel.html#object.__iter__
        """
        for property_ in self.__properties__:
            yield property_, self.__getattribute__(property_)

    ##################################################

    def __len__(self) -> int:
        """Return property count
        https://docs.python.org/3/reference/datamodel.html#object.__len__
        """
        return len(self.__properties__)

    ##################################################

    def __repr__(self) -> str:
        """Return object as json string
        https://docs.python.org/3/reference/datamodel.html#object.__repr__
        """
        return dumps(dict(self))


##################################################


if __name__ == '__main__':
    pass
