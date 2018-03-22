#this statement will cause a ZeroDivisionError
try:
	print(5/0)		
#this statement will catch the ZeroDivisionError and execute the following statements	
except ZeroDivisionError:
	print("You can't divide by zero.")	

#Exceptions to prevent crashes
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break;
	second number = input("\nSecond Number: ")
	if second_number == 'q':
		break;

	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)