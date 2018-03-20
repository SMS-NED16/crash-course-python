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
		print()

#Creating an instance of Restaurant class
restaurant = Restaurant("Marco's Bistro", "Italian")

#Printing attributes using dot operator
print("Restuarant's name is " + restaurant.restaurant_name + ".")
print("It serves " + restaurant.cuisine_type.title() + " food.")

#Printing attributes using call to describe_restaurant
restaurant.describe_restaurant();

#########################################################################
#Exercise 9.2 begins here#

#Creating three instances of Restaurant class
restaurant_1 = Restaurant("Copa Cabana", "Hawaiian")
restaurant_2 = Restaurant("Khan's of Kensington", "Pakistani")
restaurant_3 = Restaurant("Cafe Flo", "French")

#Calling describe_restaurant for each instance
print("\nPRINTING RESTAURANT DETAILS")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
