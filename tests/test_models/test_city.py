#!/usr/bin/python3
"""
unittests for city.py.
"""

import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """
    Test Cases for the City class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.city1 = City()
        self.city1.save()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.city1

    def test_initialization_user(self):
        """
        Checks if the class has attribute, empty and type string.
        """
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertEqual(self.city1.state_id, "")
        self.assertEqual(self.city1.name, "")
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city1.name), str)


if __name__ == "__main__":
    unittest.main()
