#definining a list
dimensions_list = [200, 50]

#defining a tuple
#could be dimensions of a rectangle that should 
#always be the same size
dimensions_tuple = (200, 50)	

#accessing list elements
print(dimensions_list[0])	#prints 200

#accessing tuple elements
print(dimensions_tuple[0])	#prints 200
print(dimensions_tuple[1])	#prints 50

#changing values of list
dimensions_list[0] = 300	#dimensions_list = [300, 50]
print(dimensions_list[0])	#prints 300

#changing values of a tuple
"""
dimensions_tuple[0] = 300 
#TypeError: 'tuple' object does not support item assignment
"""

#looping through a tuple
print(("Looping through a tuple").upper())
dims = (200, 500, 300)
for dimension in dims:
	print(dimension)

#Reassignment of tuples
print(("resassignment of tuples").upper())
dims = (200, 50)
print("Original dimensions:\t" + str(dims))

dims = (400, 100)	#assign new set of values to tuple variable
print("New dimensions:\t" + str(dims))


