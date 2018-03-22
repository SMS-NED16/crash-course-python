"""
Reads names of cats and dogs from cats.txt and dogs.txt respectively
Uses try-except block to deal with FileNotFound error by printing error message
"""

#Create filepaths for cats and dogs
cats_file = "text_files/cats.txt"
dogs_file = "text_files/dogs.txt"

#Attempt to read cats
try:
	with open(cats_file, encoding="utf-8") as cats_f_obj:
		cats = cats_f_obj.readlines()
except FileNotFoundError:
	print("The file " + cats_file + " could not be found.")
else:
	print("printing list of cats".upper())
	for cat in cats:
		print(cat.strip(), end=", ")
	print()

print()
#Attempt to read dogs - test except block by changing filename to doggos.txt
try:
	with open(dogs_file, encoding="utf-8") as dogs_f_obj:
		dogs = dogs_f_obj.readlines()
except FileNotFoundError:
	print("The file " + dogs_file + " could not be found.")
else:
	print("printing list of dogs".upper())
	for dog in dogs:
		print(dog.strip(), end=", ")
	print()
print("END OF PROGRAMME")