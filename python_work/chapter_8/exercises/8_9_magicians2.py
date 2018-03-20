def show_magicians(magicians_list):
	"""Print name of each magician in magicians_list"""
	if magicians_list:
		for magician in magicians_list:
			print(magician.title())
	else:
		print("No magicians in list!")

def make_great(magicians_list):
	"""add 'the Great' to beginning of each name in magicians_list"""
	new_list = []			#list to store modified names
	while magicians_list:					#while original list not empty
		magician = magicians_list.pop(0)	#remove first item from list
		magician = "The Great " + magician  #add 'the great' to this item
		new_list.append(magician)			#add this item to new_list
	return new_list			#at end, return new list

#Create a list of magicians
performing_magicians = ['david blaine', 'fussili', 'david copperfield',
	'criss angel', 'raman sharma', 'barney stinson']

#Add 'the Great' to each name
#returns modified version of list to store in original list
performing_magicians = make_great(performing_magicians)

#Print results
show_magicians(performing_magicians)
