#!/usr/bin/python3
"""
unittests for amenity.py.
"""

import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """
    Test Cases for the Amenity class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.amenity1 = Amenity()
        self.amenity1.save()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.amenity1

    def test_initialization_state(self):
        """
        Checks if the class has attribute, empty and type string.
        """
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertEqual(self.amenity1.name, "")
        self.assertEqual(type(self.amenity1.name), str)

if __name__ == "__main__":
    unittest.main()


