#!/usr/bin/python3
"""
unittests for user.py.
"""

import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """
    Test Cases for the User class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.user1 = User()
        self.user1.save()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.user1

    def test_initialization_user(self):
        """
        Checks if the class has attribute, empty and type string.
        """
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertTrue(hasattr(self.user1, "password"))
        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertTrue(hasattr(self.user1, "last_name"))
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)


if __name__ == "__main__":
    unittest.main()
