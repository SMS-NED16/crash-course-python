#Defining a Restaurant class
class Restaurant():
	"""Simple class to model a restaurant in terms of name and cuisine type"""
	def __init__(self, name, cuisine):
		"""Constructor - initialises name and cuisine type"""
		self.restaurant_name = name
		self.cuisine_type = cuisine

	def describe_restaurant(self):
		"""Prints name and cuisine type of restaurant"""
		print("Restaurant name:\t" + self.restaurant_name.title())
		print("Cuisine Type:\t" + self.cuisine_type.title())

#Creating an instance of Restaurant class
restaurant = Restaurant("Marco's Bistro", "Italian")

#Printing attributes using dot operator
print("Restuarant's name is " + restaurant.restaurant_name + ".")
print("It serves " + restaurant.cuisine_type.title() + " food.")

#Printing attributes using call to describe_restaurant
restaurant.describe_restaurant();