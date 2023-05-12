#!/usr/bin/python3
"""
unittests for file_storage.py
"""

import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest

class Test_FileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """
        Checks all() method of the FileStorage class.
        """
        self.assertTrue(type(models.storage.all()) is dict)

    
    def test_new_method(self):
        """
        Checks the new() method of the FileStorage class.
        """
        model1 = BaseModel()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + model1.id,
                      models.storage.all().keys())

    def test_save_method(self):
        """
        Checks reload() method in FileStorage class.
        """
        model1 = BaseModel()

        models.storage.save()

        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + model1.id, save_text)

    def test_reload_method(self):
        """
        Checks the reload method of the FileStorage class.
        """
        model1 = BaseModel()

        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + model1.id, objects)


if __name__ == "__main__":
    unittest.main()
