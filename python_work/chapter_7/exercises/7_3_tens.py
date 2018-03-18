#Ask user to input number
prompt = "Enter a number and I will tell you if it's a multiple of ten. "
number = input(prompt)

#Convert number to int for comparison
number = int(number)

#If number divisible by 10 
if number % 10 == 0:
	print(str(number) + " is divisible by 10.")
else:
	print(str(number) + " is not divisible by 10.")