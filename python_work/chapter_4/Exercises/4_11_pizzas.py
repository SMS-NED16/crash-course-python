#make list of pizzas
pizzas = ['Chicken Tikka', 'Golden Delight', 'Chicken Legend', 'Cheese Burst']

#copy of list of pizzas
friend_pizzas = pizzas[:]

#echoing pizzas
print(pizzas)
print(friend_pizzas)

#add pizza to original list
pizzas.append('Pepperoni')

#add pizza to friend's list
friend_pizzas.append('Chicken Supreme')

#Prove lists are separatea
print("\nMy favourite pizzas are")
for pizza in pizzas:
	print(pizza, end = " ")
print()

print("\nMy friend's favourite pizzas are")
for pizza in friend_pizzas:
	print(pizza + ",", end = " ")
print()