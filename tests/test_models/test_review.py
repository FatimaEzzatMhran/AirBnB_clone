#!/usr/bin/python3
"""
unittests for review.py.
"""

import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """
    Test Cases for the Review class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.review1 = Review()
        self.review1.save()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.review1

    def test_initialization_user(self):
        """
        Checks if the class has attribute, empty and type string.
        """
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertTrue(hasattr(self.review1, "text"))
        self.assertEqual(self.review1.place_id, "")
        self.assertEqual(self.review1.user_id, "")
        self.assertEqual(self.review1.text, "")
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.text), str)


if __name__ == "__main__":
    unittest.main()
