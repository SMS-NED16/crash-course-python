#Creating file to which we will write our message
filename = "text_files/programming.txt"

#Opening file in write mode, writing a message
#with closes file automatically when write complete
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

#Writing multiple lines
filename = "text_files/programming_2.txt"
with open(filename, 'w') as file_object:
	file_object.write("I love proramming.\n")
	file_object.write("I love creating games.\n")

#appending to a file
filename = "text_files/programming_2.txt"
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")