age = 19
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")

#if-else block
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("You are not old enough to vote.")
	print("Please register to vote as soon as you turn 18.")

#if-elif-else blocks
age = 12
if age < 4:
	print("No cost of admission.")
elif age < 18:
	print("Your cost of admission is $5.")
else:
	print("Your cost of admission is $10.")


#using if-el-if to set value for variable
age = 12
price = 0
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your age is:\t" + str(age))
print("So your cost of admission is:\t$" + str(price))


#multiple elif blocks
age = 67
if age < 4:			#if younger than 4 years old, free entry
	price = 0
elif age < 18:		#if older than 4 but youngers than 18
	price = 5			#student discount
elif age < 65:		#if older than 18 but younger than 65
	price = 10			#full price of admission
else:				#if 65 or older, 5 dollar senior discount
	price = 5
print("Your admission cost is $" + str(price) + ".")

#else block not always necessary
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5		#only runs for for valid daa

#testing multiple conditions	
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese')
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
print('\nFinished making your pizza')

#example to show when if-elif is wrong
"""This block will not print 'adding extra cheese'
even though it is present in the list of toppings
because in order for the elif statement for extra cheese
to be executed, the if block for the mushrooms must fail.
The if block for mushrooms does not fail, so the elif blocks
for both pepperoni and extra cheese are never executed."""
if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
	print('Adding extra cheese')
print('\nFinished making your pizza')
