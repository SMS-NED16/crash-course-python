#buffet programme

#Creating a TUPLE of foods served in the restaurant
foods = ("Burger", "Pizza", "Ice Cream", "Lasagne", "Sandwich")

"""
#Trying to modify one item
foods[0] = "Biryani" 	#TypeError: 'tuple' object does not support item assignment
"""

#Restaurant changes menu - creating new tuple
foods = ("Biryani", "Pizza", "Ice Cream", "Lasagne", "Cheese Platter")

#Using for loop to print revised menu
for food in foods:
	print(food)
