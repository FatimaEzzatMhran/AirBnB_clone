#!/usr/bin/python3
"""
unittests for file_storage.py
"""

import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
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
        user1 = User()
        state1 = State()
        city1 = City()
        place1 = Place()
        review1 = Review()
        amenity1 = Amenity()

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + model1.id,
                      models.storage.all().keys())
        self.assertIn(model1, models.storage.all().values())
        self.assertIn("User." + user1.id, models.storage.all().keys())
        self.assertIn(user1, models.storage.all().values())
        self.assertIn("State." + state1.id, models.storage.all().keys())
        self.assertIn(state1, models.storage.all().values())
        self.assertIn("Place." + place1.id, models.storage.all().keys())
        self.assertIn(place1, models.storage.all().values())
        self.assertIn("City." + city1.id, models.storage.all().keys())
        self.assertIn(city1, models.storage.all().values())
        self.assertIn("Amenity." + amenity1.id,
                      models.storage.all().keys())
        self.assertIn(amenity1, models.storage.all().values())
        self.assertIn("Review." + review1.id,
                      models.storage.all().keys())
        self.assertIn(review1, models.storage.all().values())

    def test_save_method(self):
        """
        Checks reload() method in FileStorage class.
        """
        model1 = BaseModel()
        user1 = User()
        state1 = State()
        city1 = City()
        place1 = Place()
        review1 = Review()
        amenity1 = Amenity()

        models.storage.save()

        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + model1.id, save_text)
            self.assertIn("User." + user1.id, save_text)
            self.assertIn("State." + state1.id, save_text)
            self.assertIn("Place." + place1.id, save_text)
            self.assertIn("City." + city1.id, save_text)
            self.assertIn("Amenity." + amenity1.id, save_text)
            self.assertIn("Review." + review1.id, save_text)

    def test_reload_method(self):
        """
        Checks the reload method of the FileStorage class.
        """
        model1 = BaseModel()
        user1 = User()
        state1 = State()
        city1 = City()
        place1 = Place()
        review1 = Review()
        amenity1 = Amenity()

        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + model1.id, objects)
        self.assertIn("User." + user1.id, objects)
        self.assertIn("State." + state1.id, objects)
        self.assertIn("Place." + place1.id, objects)
        self.assertIn("City." + city1.id, objects)
        self.assertIn("Amenity." + amenity1.id, objects)
        self.assertIn("Review." + review1.id, objects)


if __name__ == "__main__":
    unittest.main()
