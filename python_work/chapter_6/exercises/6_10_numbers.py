#making dictionary of people with favourite numbers
favourite_numbers = {
	'saad' : [1, 2, 3, 4, 5],
	'mashkoor': [1, 9, 6, 8],
	'nasreen': [3, 4, 7]
}

#Printing each name and list of favourite numbers
for name, numbers in favourite_numbers.items():
	print(name.title() + "'s favourite numbers are:\t", end = " ")
	for number in numbers:
		print("\t" + str(number), end = " ")
	print()