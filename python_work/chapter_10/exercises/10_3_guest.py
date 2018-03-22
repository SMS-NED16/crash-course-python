"""
Prompts the user for their name
Stores response in guest.txt
"""

#Creating filepath for guest.txt
filename = "text_files/guest.txt"

#prompting user to enter their name
name = input("What is your name? ")

#writing name to guest.txt
with open(filename, 'w') as file_object:
	file_object.write(name + "\n")
