#Making dictionary for each person
saad = {
	'first_name' : 'saad',
	'middle_name' : 'mashkoor',
	'last_name' : 'siddiqui',
	'age' : 21,
	'hometown' : 'karachi'
}

nasreen = {
	'first_name' : 'zarina',
	'middle_name' : '',
	'last_name' : 'nasreen',
	'age' : 59,
	'hometown' : 'karachi',
}

mashkoor = {
	'first_name' : 'mashkoor',
	'middle_name' : 'ahmed',
	'last_name' : 'siddiqui',
	'age' : 63,
	'hometown' : 'dhaka'
}

#Creating list of dictionaries
people = [saad, mashkoor, nasreen]

#Printing contents of people
for person in people:
	print(person)
	name = person['first_name'] + " " +  person['middle_name']  + " " + person['last_name']
	print("\tName:\t" + name.title())
	print("\tAge:\t" + str(person['age']))
	print("\tHome town:\t" +  person['hometown'].title())
	print()



