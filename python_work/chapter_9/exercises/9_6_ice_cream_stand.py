#Superclass - Restaurant
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

	def get_people_served(self, number):
		"""Prints number of people served"""
		print("Customers served today:\t" + str(self.people_served))

	def reset_people_served(self, number):
		"""
		Resets the number of people served to 0
		To be used at the beginning or end of each business day
		"""
		self.people_served = 0

#Subclass - Ice Cream Stand
class IceCreamStand(Restaurant):
	"""Simple attempt to model an Ice Cream Stand, which is a kind of Restaurant"""
	def __init__(self, name, cuisine, *flavours):
		"""
		Initialises all member attributes of parent class
		Then initialises all member attributes of child class
		"""
		super().__init__(name, cuisine)
		self.flavours = flavours 	

	def display_flavours(self):
		"""Display list of flavours served by the restaurant"""
		print("List of flavours served by " + self.restaurant_name.title())
		for flavour in self.flavours:
			print(flavour.title(), end = ", ")


#Creating an instance of the IceCreamStand class
snoopy = IceCreamStand("Snoopy's", "Ice Cream",
	 "vanilla", "strawberry", "mint chocolate chip, mango")

snoopy.describe_restaurant()
snoopy.display_flavours()

