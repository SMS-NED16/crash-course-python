import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for name_function.py module"""

	def test_first_last_name(self):
		"""Do names like 'Janice Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()