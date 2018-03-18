info = "Movie ticket prices".upper()
info += "\nLess than three years: free"
info += "\nBetween 3 and 12 years: $10"
info += "\nOver 12 years: $15"

prompt = info + "\nEnter your age. Enter -1 to quit. "
age = 0

""" Using conditional in while loop
while int(age) != -1:
	age = input(prompt)
	age = int(age)
	if age >= 0 and age < 3:
		print("Your ticket price: free!\n")
	elif age >= 3 and age <= 12:
		print("Your ticket price: $10\n")
	elif age > 12:
		print("Your ticket price: $15\n")
print("END OF PROGRAMME")
"""

""" using break statement
while True:
	age = input(prompt)
	age = int(age)
	if age == -1:
		break
	else:
		if age >= 0 and age < 3:
			print("Your ticket price: free!\n")
		elif age >= 3 and age <= 12:
			print("Your ticket price: $10\n")
		elif age > 12:
			print("Your ticket price: $15\n")
print("END OF PROGRAMME")
"""

#using active flag
active = True	#create flag - initially true
while active:
	age = input(prompt)
	age = int(age)
	if age == -1:
		active = False;
	else:
		if age >= 0 and age < 3:
			print("Your ticket price: free!\n")
		elif age >= 3 and age <= 12:
			print("Your ticket price: $10\n")
		elif age > 12:
			print("Your ticket price: $15\n")
print("END OF PROGRAMME")
