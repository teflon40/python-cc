#!/usr/bin/python3

import unittest
from city_functions import f_city_function

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        city_name = f_city_function('santiago', 'chile')
        self.assertEqual(city_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test for an optional parameter"""
        city_name = f_city_function('santiago', 'chile', population=5000000)
        self.assertEqual(city_name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
