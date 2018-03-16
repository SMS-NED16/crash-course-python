#Generating list of squares without list comprehension
squares_1 = []
for val in range(1, 11):
	squares_1.append(val ** 2)
print(squares_1)

#Generating list of squares with list comprehension
squares_2 = [value ** 2 for value in range(1, 11)]
print(squares_2)
