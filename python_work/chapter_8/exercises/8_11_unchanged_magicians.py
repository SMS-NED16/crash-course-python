def show_magicians(magicians_list):
	"""Prints each name in list"""
	for magician in magicians_list:
		print(magician.title())

def make_great(magicians_list):
	"""Prepends 'the Great' to each name in list"""
	"""Adds this new name to a new list"""
	new_list = []
	while magicians_list:
		name = magicians_list.pop(0)
		name = 'The Great ' + name
		new_list.append(name)
	return new_list

magicians = ['david copperfield', 'david blaine', 'barney stinson', 'fussili']
modified_magicians = make_great(magicians[:])

print("Printing names in 'magicians'".upper())
show_magicians(magicians)

print("\nPrinting names in 'modified_magicians'".upper())
show_magicians(modified_magicians)

