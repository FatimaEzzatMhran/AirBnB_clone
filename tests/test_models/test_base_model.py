#!/usr/bin/python3
"""
unittests for base_model.py.
"""

from datetime import datetime
import models
from models.base_model import BaseModel
import unittest
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the BaseModel Class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.model1
        del self.model2

    def test_BaseModel_instance_has_id(self):
        """
        Checks whether the BaseModel instance has an id assigned by init
        """
        self.assertTrue(hasattr(self.model1, "id"))

    def test_id(self):
        """
        Checks whether the id of the base model of type str.
        """
        self.assertEqual(type(self.model1.id), str)

    def test_created_at(self):
        """
        Checks whether the created_at attribute of type datetime obj
        """
        self.assertEqual(type(self.model1.created_at), datetime)

    def test_updated_at(self):
        """
        Checks whether the updated_at attribute of type datetime obj
        """
        self.assertEqual(type(self.model1.created_at), datetime)

    def test_uuid_is_different(self):
        """
        Checks whehter each id for obj is unique.
        """
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_kwargs(self):
        """
        Checks if instance with kwargs correctly sets attrs.
        """
        kwargs = {"id": "390",
                  "created_at": "2022-12-05T12:12:12.555555",
                  "anykey": "value of anykey"}
        model3 = BaseModel(**kwargs)
        self.assertEqual(model3.id, "390")
        self.assertEqual(model3.created_at,
                         datetime.fromisoformat
                         ("2022-12-05T12:12:12.555555"))
        self.assertEqual(model3.anykey, "value of anykey")

    def test_args_and_kwargs(self):
        """
        Checks when args and kwargs are passed.
        """
        model5 = BaseModel("55", id="77")
        self.assertEqual(model5.id, "77")

    def test_str(self):
        """
        Checks the __str__method.
        """
        model6 = BaseModel()
        model6_str = f"[{model6.__class__.__name__}] "\
            f"({model6.id}) {model6.__dict__}"
        self.assertEqual(str(model6), model6_str)

    def test_save(self):
        """
        Checks if save method updates the updated_at attr.
        """
        old_updated_at = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(old_updated_at, self.model1.updated_at)

    def test_to_dict(self):
        """
        Checks whehter the to_dict method returns correct attrs.
        """
        kwargs = {"id": "780",
                  "created_at": "2022-11-05T12:12:12.555555",
                  "anykey": "value of anykey",
                  "updated_at": "2022-11-05T12:12:12.555555"}
        model7 = BaseModel(**kwargs)
        mydict = model7.to_dict()
        self.assertEqual(mydict["id"], "780")
        self.assertEqual(mydict["created_at"], "2022-11-05T12:12:12.555555")
        self.assertEqual(mydict["__class__"], "BaseModel")
        self.assertEqual(mydict["anykey"], "value of anykey")
        self.assertEqual(mydict["updated_at"], "2022-11-05T12:12:12.555555")


if __name__ == "__main__":
    unittest.main()
