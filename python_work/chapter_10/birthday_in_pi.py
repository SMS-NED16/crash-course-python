"""Programme to find if birthday in mmddyy format appears in pi"""

#filename to store path of file containing million digits of pi
filename = "text_files/pi_million_digits.txt"

#read file, store lines in list, close when complete
with open(filename) as file_object:
	lines = file_object.readlines()

#Create one string containing all digits of pi
pi_string = ' '
for line in lines:
	pi_string += line.strip()

#Ask user to input birthday
birthday = input("Enter your birthday in the form mmddyy: ")

#search for birthday in pi_string and print message if found
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
