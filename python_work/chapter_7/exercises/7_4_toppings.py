prompt = "Enter name of topping to add to your pizza."
prompt += "\nEnter 'quit' when you are done.\t"

user_input = ""

while user_input.lower() != 'quit':
	user_input = input(prompt)
	if user_input.lower() != 'quit':
		print("Will add " + user_input.title() + " to your pizza.\n")
print("Done adding toppings to your pizza.")