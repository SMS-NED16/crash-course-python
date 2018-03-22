"""
Replacing every instance of 'Python' in learning_python.txt with 'C'
"""

#storing filepath
filename = "text_files/learning_python.txt"

#opening file, reading data, storing in list, closing file when finished
with open(filename) as file_object:
	lines = file_object.readlines()

#for every line in list of lines
for line in lines:
	#Replace Python with C++, store modified line in place of original
	line = line.replace("Python", "C++")	
	#Print modified line after stripping whitespace
	print(line.strip())