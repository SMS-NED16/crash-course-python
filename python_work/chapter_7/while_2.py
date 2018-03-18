#Start with users that need to be verified
# and an empty list to hold confirmed users

"""
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users
#Move each verified user into the list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
	print("unconfirmed_users at end of verification")
	print(unconfirmed_users)

#Display all confirmed users
print("\nThe following users have been confirmed.")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#removing all instances of a value from a list
print("\nremoving all instances of a value from a list".upper())
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
"""

#filling dictionary with user input
print("\nfilling a dictionary with user input".upper())
responses = {}	#empty dictionary to store name-response key-value pairs
polling_active = True	#set a flag to indiciate polling is active

while polling_active:
	#prompt for the person's name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	#store the response in the dictionary
	responses[name] = response

	#Find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat.lower() == 'no':
		polling_active = False

#Polling is complete. Show results
print("\n---- POLL RESULTS ----")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + ".")

