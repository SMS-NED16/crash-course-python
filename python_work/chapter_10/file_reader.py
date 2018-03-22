#reading entire file
print("Reading an entire file".upper())
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)


#reading entire file, removing trailing whitespace
print("\nReading an entire file. Removing whitespace".upper())
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())


#reading entire file - relative paths
print("\nReading an entire file using a relative path".upper())
with open('text_files/pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())


#reading entire file - absolute path
print("\nReading an entire file using an absolute path".upper())
filepath = "/Users/saadmashkoor/Desktop/pi_digits.txt"
with open(filepath) as file_object:
	contents = file_object.read()
	print(contents.rstrip())


#reading a file one line at a time
filename = "text_files/pi_digits.txt"
print("\nReading a file one line at a time".upper())
with open(filename) as file_object:
	for line in file_object:
		print(line)


#Reading a file one line at a time
#also removing whitespace due to extra \n character at end of each line
filename = "text_files/pi_digits.txt"
print("\nReading a file one line at a time".upper())
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


#making a list of lines from a file
filename = "text_files/pi_digits.txt"
print("\nReading all lines in file and storing them in list".upper())
with open(filename) as file_object:
	lines = file_object.readlines()

#The list of lines is now available for processing outside the with block
for line in lines:
	print(line.rstrip())


#working with a file's contents
print("\nWorking with a file's contents".upper())
filename = "text_files/pi_digits.txt"
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''	#empty string to store lines
for line in lines:
	pi_string += line.rstrip()	#does not remove whitespace from left end
print(pi_string)
print(len(pi_string))

#working with a file's contents - improved whitepsace elimination
print("\nWorking with a file's contents".upper())
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))
