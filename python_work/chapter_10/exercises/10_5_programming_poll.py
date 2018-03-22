"""
Asks users to enter their resaons for liking programming
Stores responses in a file called 'responses.txt'
"""

filename = "text_files/responses.txt"

entry_flag = True

while entry_flag:
	print("Welcome to our programming survey. Enter 'q' to quit at any time.")
	user_response = input("Why do you like programming? ")
	if user_response.lower() == 'q':
		print("Thank you for taking our survey!\n")
		entry_flag = False
	else:
		print("Thank you for taking our survey!\n")
		with open(filename, 'a') as file_object:
			file_object.write(user_response + "\n")
