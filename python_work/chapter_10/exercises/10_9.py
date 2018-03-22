"""
Improved version of the programme in 10_9_cats_dogs.py
try-except-else block has been wrapped into a function
Also fails silently with a pass statement in except
"""

def print_list(filename):
	try:
		with open(filename, encoding="utf-8") as file_object:
			content = file_object.readlines()
	except FileNotFoundError:
		pass
	else:
		print("Reading data from " + filename + ".")
		for line in content:
			print(line.strip(), end = ", ")
		print("\n")


print_list("text_files/cats.txt")
print_list("text_files/doggos.txt")

#Test silent except block
print_list("text_files/dogs.txt")

print("End of programme")