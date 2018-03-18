#Ask user to enter number of guests in dinner group
number_of_guests = input("How many people are in your dinner group? ")

#Convert number to numeric for comparison
number_of_guests = int(number_of_guests)

#Print appropriate message
if number_of_guests > 8:
	print("You will have to wait for a table.")
else:
	print("Your table is ready! Please follow me.")