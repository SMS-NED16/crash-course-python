"""A class that can be ued to represent a restaurant"""

class Restaurant():
	"""Simple class to model a restaurant in terms of name cuisine type"""
	def __init__(self, name, cuisine):
		"""Constructor - initialises name and cuisine type"""
		self.restaurant_name = name
		self.cuisine_type = cuisine
		self.people_served = 0		#default value

	def describe_restaurant(self):
		"""Prints a neatly formatted string describing restaurant"""
		print("The restaurant's name is " + self.restaurant_name + ".")
		print("Food served:\t" + self.cuisine_type)
		print("People served:\t" + str(self.people_served)) 


	def set_people_served(self, number):
		"""
		Sets number of customers served to value specified by user
		Prevents roll back of customers served in a day
		"""
		if number >= self.people_served:
			self.people_served = number
		else:
			print("Can't unserve customers!")

	def get_people_served(self):
		"""Prints number of people served"""
		print("Customers served today:\t" + str(self.people_served))

	def reset_people_served(self):
		"""
		Resets the number of people served to 0
		To be used at the beginning or end of each business day
		"""
		self.people_served = 0