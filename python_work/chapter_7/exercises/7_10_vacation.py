#Empty dictionary to store name-destination key-value pairs for survey
vacation_responses = {}

polling_active = True

while polling_active:
	name = input("What is your name? ")
	destination = input("If you could visit one place in the world "
		+ "where would you go? ")
	vacation_responses[name] = destination
	continue_prompt = "\nIs there any one else who'd like to take the survey?"
	continue_prompt += "\n(yes/no) "
	continue_polling = input(continue_prompt)
	if continue_polling.lower() == 'no':
		polling_active = False

for name, destination in vacation_responses.items():
	print(name.title() + " would like to visit " + destination.title() + ".")
