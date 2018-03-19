#first function
def greet_user():
	"""Display a simple greeting"""
	print("Hello!")


#passing information to a funciton
def greet_user_1(username):
	"""Display a simple greeting with the username"""
	print("Hello, " + username.title() + "!")

#call greet_user
greet_user()

#call greet_user_1
greet_user_1("Saad")
greet_user_1("jesse")

