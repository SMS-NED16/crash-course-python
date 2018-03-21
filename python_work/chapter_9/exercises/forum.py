"""A module which contains classes that can be used for forum users"""

class User():
	"""A class that models a user for an online forum"""
	def __init__(self, f_name, l_name,
				 age, city, hometown, *languages):
		"""Constructor - creates attributes, initialises them"""
		self.first_name = f_name;
		self.last_name = l_name;
		self.age = age
		self.city = city
		self.hometown = hometown
		self.languages = languages   	#languages is a tuple

	def describe_user(self):
		"""Prints all information about user as a neatly formatted string"""
		print("Name:\t" + self.first_name.title() 
			+ " " + self.last_name.title())
		print("Age:\t" + str(self.age))
		print("City:\t" + self.city)
		print("Hometown:\t" + self.hometown)
		print("Languages:\t" + str(self.languages))

	def greet_user(self):
		"""Displays a personalised greeting for the user"""
		print("Hello, " + self.first_name.title() + "! Welcome back!")

class Privileges():
	"""A class that is used to describe user privileges/actions for a forum"""
	def __init__(self, *list_of_privileges):
		self.actions_allowed = list_of_privileges

	def show_privileges(self):
		print("This user has the following privileges.")
		for privilege in self.actions_allowed:
			print(" -" + privilege)

class Admin(User):
	"""A specialised version of the User class for forum administrators"""
	def __init__(self, f_name, l_name, age, city, hometown, *languages):
		"""Initialises superclass attributes, then inits privileges"""
		super().__init__(f_name, l_name, age, city, hometown, *languages)
		self.privileges = Privileges("can add post", "can delete post", "can ban user")


