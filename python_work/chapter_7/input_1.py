#ask the user to enter text; echo text back to user as message
"""message = input("Please enter some text.")
print(message)

#writing clear prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")


#multiline prompts
prompt = "If you tell us who you are, we can perzonalise the messages you will see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
"""
"""
age = input("How old are you? ")
age = int(age)
if age >= 18:
	print("You are old enough to vote.")
else:
	print("Sorry. You need to wait for " + str(18 - age) + 
		" years to be vote!")

height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride!")
else:
	print("\nYou will be able to ride when you're a little older.")
"""

#Even/Odd with Modulo Operator
number = input("Enter a number and I will tell you if it is even or odd. ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")
