"""
#Using while loop to count from 1 to 5
current_number = 1;
while current_number <= 5:
	print(current_number, end = " ")
	current_number += 1
print("\nEnd of while loop")
"""

"""
#Using while loop for echoing messages
prompt = " \nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "	#defining quit value in prompt

message = ""
while message.lower() != 'quit':
	message = input(prompt)
	if message.lower() != 'quit':
		print(message)
"""

#Using flags with loops
"""
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the programme. "

active = True
while active:
	message = input(prompt)
	if message.lower() == 'quit':
		active = False;
	else:
		print(message)
print("End of while loop".upper())
"""

#Using break

"""
prompt = "Please enter the name of a city you have visited."
prompt += "\nEnter 'quit' when you are finished. "

while True:
	city = input(prompt)
	if city.lower() == 'quit':
		break		
	else:
		print("I'd love to go to " + city.title() + ".")
		print()		#new line at end of input
"""

#using continue
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number, end = " ")
print("\n")

