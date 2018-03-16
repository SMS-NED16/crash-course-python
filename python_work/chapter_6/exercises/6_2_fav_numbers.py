#creating dictionary to store favourite numbers of different people
favourite_numbers = {
	'saad' : 0,
	'mashkoor' : 1,
	'nasreen' : 11,
	'siddiqui' : 35 
}

#printing each member's name and favourite number
if favourite_numbers:
	for key in favourite_numbers:
		print(key.title() + "'s favourite number is " +
			str(favourite_numbers[key]) + ".")
else:
	print("No data in dictionary.")
