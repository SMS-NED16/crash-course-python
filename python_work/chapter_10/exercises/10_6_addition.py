"""Addition with exception handling"""

num_1 = input("Enter the first number.")
num_2 = input("Enter the second number.")
try:
	num_1 = int(num_1)
	num_2 = int(num_2)
except ValueError:		#does not work with TypeError
	print("Please enter numbers only. No text or characters.")
else:
	print(str(num_1) + " + " +  str(num_2) + " = " + str(num_1 + num_2))