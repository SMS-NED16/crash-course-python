import unittest
from city_functions import get_location

class CityFunctionsTest(unittest.TestCase):
	"""Tests for the module city_functions.py"""

	def test_city_country(self):
		"""Does the get_location return output like 'Karachi, Pakistan'?"""
		location_string = get_location('santiago', 'chile')
		self.assertEqual(location_string, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Does get_location return output like 'Karachi, Pakistan, 500000'"""
		location_string = get_location('santiago', 'chile', 5000000)
		self.assertEqual(location_string, 
			"Santiago, Chile - population 5000000")

		
unittest.main()