#Creating a list of cars, all in lowercase 
cars = ['audi', 'bmw', 'subaru', 'toyota']

#looping through cars list
for car in cars:
	if car == 'bmw':		#if current car is 'bmw'
		print(car.upper())		#print in all caps
	else:					#otherwise
		print(car.title())		#print with first letter capitalised
print()

#CONDITIONALS
car = 'bmw'
print(car=='bmw')
print(car=='audi')

#Ignoring Case When Checking for Equality
car_2 = 'Audi'
print(car_2.lower() == 'audi')
car_2 = 'aUdI'
print(car_2.lower() == 'audi')

car_3 = 'Subaru'
print(car_3.lower() == 'subaru')
print(car_3 + "\n")

#Inequality Operator
requested_topping = 'mushrooms'
if(requested_topping != 'anchovies'):
	print("Hold the anchovies!")

#Numerical Comparisons
age = 18
print(age == 18)
print(age == 324)

answer = 17
if answer != 42:
	print("This not the correct answer. Please try again.")

#Combinining conditionals
age_0 = 22
age_1 = 18
if (age_0 >= 21 and age_1 >= 21):
	print("Both ages are above 21.")
else:
	print("At least one age is below 21.")

#in keyword
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#not in keyword
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if (user not in banned_users):
	print(user.title() + " is allowed to comment in the forum")