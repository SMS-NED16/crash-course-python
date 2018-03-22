"""
An improved version of 10_6_addition.py
Which allows users to re-enter entering data
If they enter invalid values the first time
"""

continue_entry = True	#flag changes to false when valid values entered

while continue_entry:	#continue until valid input received
	#get input
	num_1 = input("Enter the first number: ")
	num_2 = input("Enter the second number: ")
	
	#try typecasting to int for addition
	try:					
		num_1 = int(num_1)		
		num_2 = int(num_2)

	#in case of ValueError (unsuccessful typecast)
	except ValueError:
		print("One or more invalid values. Please re-enter data.")
	
	#otherwise, print result of addition and change flag value to exit loop
	else:
		result = num_1 + num_2
		print(str(num_1) + " + " + str(num_2) + " = " + str(result))
		continue_entry = False;
