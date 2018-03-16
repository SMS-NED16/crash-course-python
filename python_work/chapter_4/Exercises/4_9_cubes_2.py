#used list comprehension in last one so will use other syntax
cubes_1 = []

for num in range(1,11):
	cubes_1.append(num ** 3)

for cube in cubes_1:
	print(cube, end = " ")
print()