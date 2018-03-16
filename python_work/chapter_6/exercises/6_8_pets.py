#Making dictionaries to store pet details
chubby = {
	'name' : 'chubby',
	'type' : 'cat',
	'owner': 'saad',
}

borko = {
	'name' : 'borko',
	'type' : 'dog',
	'owner': 'siddiqui',
}

fluff_face = {
	'name' :'fluff face',
	'type' : 'rabbit',
	'owner' : 'nasreen',
}

#Making list of pets
pets = [chubby, borko, fluff_face]

#Parsing list, printing pet details
for pet in pets:
	print(pet)
	print("\tName:\t" + pet['name'].title())
	print("\tType:\t" + pet['type'].title())
	print("\tOwner:\t" + pet['owner'].title())
	print()