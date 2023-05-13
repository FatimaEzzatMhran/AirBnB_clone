#!/usr/bin/python3
"""
unittests for state.py.
"""

import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """
    Test Cases for the State class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.state1 = State()
        self.state1.save()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.state1

    def test_initialization_state(self):
        """
        Checks if the class has attribute, empty and type string.
        """
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertEqual(self.state1.name, "")
        self.assertEqual(type(self.state1.name), str)


if __name__ == "__main__":
    unittest.main()
