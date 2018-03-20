"""Passing lists as arguments to functions"""
def greet_users(names):		#names is a list
	"""Print a simple greeting to each name in list 'names'"""
	for name in names:
		msg = "Hello, " + name.title() + "! Nice to meet you." 
		print(msg)

#Create list of names
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

"""Using functions to modify list data"""
#Start with some designs that need to printed 
"""print("\nModifying list without a function".upper())
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design until none left
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("Printing model: " + current_design)
	completed_models.append(current_design)

#Display all completed models
print("\nThe following models have been printed")
for completed_model in completed_models:
	print(completed_model)
"""

"""Using functions to modify list data"""
def print_models(unprinted_designs, completed_models):
	"""

	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#simulate creating a 3d print from the design
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed"""
	print("\nThe following models have been printed.")
	for completed_model in completed_models:
		print(completed_model)

#Main part of the programme - more concise, easier to understand
orders_to_print = ['iphone case', 'robot pendant', 'dodecahedron']
completed_prints = []

print_models(orders_to_print, completed_prints)
show_completed_models(completed_prints)


"""Preventing a function from modifying a list"""
print("\n\nPreventing a function from modifying a list".upper())
orders_to_print = ['iphone case', 'robot pendant', 'dodecahedron']
completed_prints = []
print_models(orders_to_print[:], completed_prints)
show_completed_models(completed_prints)
print("print_models at end of function call:\t" + str(orders_to_print))
print("completed models at end of function call:\t" + str(completed_prints))