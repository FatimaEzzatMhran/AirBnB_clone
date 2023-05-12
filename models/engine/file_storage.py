#!/usr/bin/python3
"""
contains the file_storage class.
"""

import json
import os

from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes a JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only of the JSON file exists; else, do nothing)
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
