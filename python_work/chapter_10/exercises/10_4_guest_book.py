"""
Asks guests to enter their names and prints greetings in response
Also stores every name in a txt file 
"""

filename = "text_files/guest_log.txt"

entry_flag = True

while entry_flag:
	name = input("Please enter your name. ('q' to quit): ")	#prompt for input
	if name.lower() == 'q':	#if user decides to quit
		entry_flag = False;		#exit entry loop
	else:										
		print("Welcome, " + name.title() + "!")		#print message
		with open(filename, 'a') as file_object:	#open file, append input
			file_object.write(name.lower() + "\n")

print("End of programme".upper())