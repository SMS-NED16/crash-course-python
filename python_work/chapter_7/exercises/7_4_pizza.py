user_input = ""
while user_input.lower() != 'quit':
	user_input = input("What topping would you like to add to your pizza? ")
	if user_input.lower() != 'quit': 
		print("Adding " + user_input.title() + " to your pizza.")
