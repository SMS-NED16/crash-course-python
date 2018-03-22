"""
Programme that reads data in file 'learning_python.txt'
and prints the file's data in three different ways
"""

#Store filepath as a variable
filename = "text_files/learning_python.txt"

#Printing data by reading entire file 
print("Reading entire file".upper())
with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

#Printing data by reading one at a time
print("\nReading data one line at a time".upper())
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#Printing data by using readlines to create list, 
#and printing list outside with block
print("\nPrinting data by using readines to create ".upper() +  
	"a list of all lines".upper())
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())
