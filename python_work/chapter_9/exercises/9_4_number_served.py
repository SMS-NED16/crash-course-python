#Defining a Restaurant class
class Restaurant():
	"""Simple class to model a restaurant in terms of name and cuisine type"""
	def __init__(self, name, cuisine):
		"""Constructor - initialises name and cuisine type"""
		self.restaurant_name = name
		self.cuisine_type = cuisine
		self.number_served = 0		#new attribute, default init zero

	def describe_restaurant(self):
		"""Prints name and cuisine type of restaurant"""
		print("Restaurant name:\t" + self.restaurant_name.title())
		print("Cuisine Type:\t" + self.cuisine_type.title())
		print("Number served:\t" + str(self.number_served))

	def set_number_served(self, number):
		"""
		Sets number_served attribute to value specified by user
		Prints error message if number 'unserves' customers/rolls
		"""
		if number >= self.number_served:
			self.number_served = number
		else:
			print("Can't un-serve customers lol")
			print("number must be greater than current served customers.")

	def increment_number_served(self, number):
		"""
		Increment the number_served by the specified amount
		Prints error message in case of negative increment
		"""
		if number >= 0 :
			self.number_served += number
		else:
			print(number + " is negative.")
			print("Negative increments not allowed.")


#Creating an instance of Restaurant class
restaurant = Restaurant("Marco's Bistro", "Italian")

#Printing attributes using dot operator
print("Restuarant's name is " + restaurant.restaurant_name + ".")
print("It serves " + restaurant.cuisine_type.title() + " food.")

#Printing attributes using call to describe_restaurant
restaurant.describe_restaurant()

#Modifying number served
restaurant.set_number_served(150)
print("\nAfter setting number_served to 150")
restaurant.describe_restaurant()

restaurant.increment_number_served(100)
print("\nAfter increment_number_served by 100")
restaurant.describe_restaurant()

