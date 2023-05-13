#!/usr/bin/python3
"""
unittests for place.py.
"""

import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """
    Test Cases for the Place class.
    """

    def setUp(self):
        """
        Instantiate an object before running each test.
        """
        self.place1 = Place()
        self.place1.save()

    def tearDown(self):
        """
        Tears down an object after running each test.
        """
        del self.place1

    def test_initialization_user(self):
        """
        Checks if the class has attribute, empty and type string.
        """
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertTrue(hasattr(self.place1, "amenity_ids"))

        self.assertEqual(self.place1.city_id, "")
        self.assertEqual(self.place1.user_id, "")
        self.assertEqual(self.place1.name, "")
        self.assertEqual(self.place1.description, "")
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertEqual(self.place1.amenity_ids, [])


        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night,), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)



if __name__ == "__main__":
    unittest.main()
