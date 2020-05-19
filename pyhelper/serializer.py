#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan PyHelper package.

 (c) "Matthias Morin" <mat@tangoman.io>

 This source file is subject to the MIT license that is bundled
 with this source code in the file LICENSE.
"""

from json import (dumps, loads)
from typing import Any

from pyhelper.annotations import Annotations


class Serializer:
    """
    Serializer
    ==========

    - Encoder:      Encode dictionary: Hydrate object and return serialized object as json
    - Decoder:      Decode json serialized string: Hydrate object and return dictionary
    - Serializer:   Serialize object: return serialized object as json
    - Deserializer: Deserialize object: return object from json
    - Normalizer:   Normalize object: return object as dictionary
    - Denormalizer: Denormalize dictionary: Hydrate object from dictionary
    """

    ##################################################
    # Constructor
    ##################################################

    def __init__(self, object: Any) -> None:
        self.object = object
        self.annotations = Annotations(object)

    ##################################################
    # Encoder
    ##################################################

    def encode(self, dictionary: dict) -> str:
        """Encode dictionary: return serialized object as json"""
        if not isinstance(dictionary, dict):
            raise TypeError(f'{self.__class__.__name__}.encode: must be set to a dictionary')
        if dictionary == {}:
            raise ValueError(f'{self.__class__.__name__}.encode: dictionary cannot be empty')
        self.denormalize(dictionary)
        return self.serialize()

    ##################################################
    # Decoder
    ##################################################

    def decode(self, string: str) -> dict:
        """Decode json serialized string: Hydrate object and return dictionary"""
        if not isinstance(string, str):
            raise TypeError(f'{self.__class__.__name__}.decode: must be set to a string')
        if string == '':
            raise ValueError(f'{self.__class__.__name__}.decode: string cannot be empty')
        self.deserialize(string)
        return self.normalize()

    ##################################################
    # Serializer
    ##################################################

    def serialize(self) -> str:
        """Serialize object: return serialized object as json"""
        return dumps(self.normalize())

    ##################################################
    # Deserializer
    ##################################################

    def deserialize(self, string: str):
        """Deserialize object: return object from json"""
        if not isinstance(string, str):
            raise TypeError(f'{self.__class__.__name__}.deserialize: must be set to a string')
        if string == '':
            raise ValueError(f'{self.__class__.__name__}.deserialize: string cannot be empty')
        return self.denormalize(loads(string))

    ##################################################
    # Normalizer
    ##################################################

    def normalize(self) -> dict:
        """Normalize object: return object as dictionary"""
        dictionary = {}
        for property_ in self.annotations.get_properties:
            dictionary[property_] = self.object.__getattribute__(property_)
        return dictionary

    ##################################################
    # Denormalizer
    ##################################################

    def denormalize(self, dictionary: dict):
        """Denormalize dictionary: Set object properties from dictionary
        raises AttributeError when attempting to set unknown attribute
        """
        if not isinstance(dictionary, dict):
            raise TypeError(f'{self.__class__.__name__}.denormalize: must be set to a dictionary')
        if dictionary == {}:
            raise ValueError(f'{self.__class__.__name__}.denormalize: dictionary cannot be empty')
        # dictionary keys must match object properties
        for property_ in dictionary.keys():
            if property_ not in self.annotations.get_properties:
                raise AttributeError(f'{self.object.__class__.__name__} has no attribute {property_}')
        # setting given attributes from dictionary (using appropriate setters)
        for key_, value_ in dictionary.items():
            setattr(self.object, key_, value_)
        return self.object


##################################################

if __name__ == '__main__':
    pass
