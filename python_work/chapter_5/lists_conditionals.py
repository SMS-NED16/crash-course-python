#USING LISTS WITH CONDITIONAL STATEMENTS

#Simple for loop to print elements in list
print(("Checking for special items").upper())
requested_toppings  = ['mushrooms', 'extra cheese', 'green peppers']
for topping in requested_toppings:
	print('Adding ' + str(topping) + ' to pizza.')
print("Finished making your pizza.\n\n")

#If restaurant is out of green peppers
print(("Adding a conditional to the for loop.").upper())
for topping in requested_toppings:
	if topping == 'green peppers':
		print("Sorry! We are out of green peppers right now.")
	else:
		print("Added " + topping + " to your pizza.")
print("\nFinished making your pizza.")

#Checking if a list is empty
requested_toppings = []		#list of toppings init to empty list
if requested_toppings:		#if this list is not empty
	for topping in requested_toppings:
		print("Adding " + topping + " to your pizza.")
else:					
	print("Are you sure you want a plain pizza?")

#Using multiple lists
print(("\n\nUsing multiple lists").upper())
available_toppings = ['mushrooms', 'olives', 'green peppers',
						'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + " to your pizza.")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza.")