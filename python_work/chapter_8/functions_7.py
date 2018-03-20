#arbitrary number of arguments
def make_pizza(*toppings):
	"""Print list of toppings that have been requested"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
make_pizza('mushrooms', 'pepperoni', 'onions', 'olives', 'sriracha sauce')

def make_pizza_2(*toppings):
	"""Summarize the pizza we are about to make"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza_2('pepperoni')
make_pizza_2('mushrooms', 'green peppers', 'extra cheese')

#Positional and arbitrary arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make"""
	print("\nMaking a " + str(size) + "-inch pizza"
		+ " with the following toppings")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n\n\n\n")

#Aribitrary keyword arguments
print("Making dictionaries using arbitrary keyword arguments".upper())
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about the user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', 
							location = 'princeton',
							field = 'physics')
isaac_newton = build_profile('isaac', 'newton', 
							location = 'cambridge', 
							field = 'physics',
							known_for = 'calculus',
							other_contribution = ['gravity', 'lenses'])
print(user_profile)
print(isaac_newton)