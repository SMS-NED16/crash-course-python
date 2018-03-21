from user import User

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
