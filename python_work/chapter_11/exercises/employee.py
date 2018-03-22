"""A module that stores an Employee class"""

class Employee():
	"""A simple class that can be used to model an employee"""
	def __init__(self, first, last, salary):
		"""Creates employee, initialises attributes"""
		self.first_name = first
		self.last_name = last
		self.annual_salary = salary

	def give_raise(self, increment=5000):
		"""Increments annual salary by 5k unless otherwise specified"""
		self.annual_salary += increment




