"""A set of classes used to represent Electric Cars"""
from car import Car

class Battery():
	"""A simple attempt to model a battery for an electric car"""
	def __init__(self, battery_size=70):
		"""Initialise the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approxmately " + str(range) 
		message += " miles on a full charge."
		print(message)


class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""
		Initialise the attributes of the parent class
		Then initialise attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


#Creating an instance of the ElectricCar class
my_tesla = ElectricCar('testla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
