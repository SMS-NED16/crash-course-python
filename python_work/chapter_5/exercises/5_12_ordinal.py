#store numbers 1 - 9 in a list
numbers = list(range(1, 10))

#loop through list, output ordinal number for each
for number in numbers:	
	if number == 1:			#diff suffix for 1
		print ("1st")
	elif number == 2:		#diff suffix for 2
		print("2nd")
	elif number == 3:		#diff suffix for 3
		print("3rd")
	elif number > 3 and number <= 10:	#same suffix for others
		print(str(number) + "th")


