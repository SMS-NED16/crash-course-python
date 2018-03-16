#making list of cubes
cubes = [val ** 3 for val in range(1, 11)]

#printing cubes with for loop
for cube in cubes:
	print(cube, end = " ")
print()