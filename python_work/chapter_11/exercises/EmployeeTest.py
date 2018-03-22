import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""
	def setUp(self):
		"""
		Creates an instance of an employee and a raise for use in all test methods
		"""
		self.test_employee = Employee("John", "Doe", 60000)
		self.default_salary = self.test_employee.annual_salary
		self.default_raise = 5000
		self.test_raise = 10000

	def test_give_default_raise(self):
		"""Does give_raise() increment annual salary by 5000?"""
		self.test_employee.give_raise()
		self.assertTrue(self.test_employee.annual_salary, 
			self.default_salary + self.default_raise)

	def test_give_custom_raise(self):
		"""Does give_raise(10000) increment annual salary by 10000?"""
		self.test_employee.give_raise(self.test_raise)
		self.assertTrue(self.test_employee.annual_salary, 
			self.default_salary + self.test_raise )

unittest.main()
