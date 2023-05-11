#!/usr/bin/python3
"""
unittests for base_model.py.
"""

from datetime import datetime
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the BaseModel Class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.model1 = BaseModel()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.model1


if __name__ == "__main__":
    unittest.main() """
