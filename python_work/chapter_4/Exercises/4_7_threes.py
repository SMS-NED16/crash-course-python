#list of multiples of 3
threes = [num * 3 for num in range(1, 11)]

#printing list
print(threes)

#printing with for loop
for num in threes:
	print(num, end = " ")
print()

#using range syntax
threes_2 = list(range(3, 33, 3))

print(threes_2)