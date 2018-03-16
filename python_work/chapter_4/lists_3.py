#range function - print 1 to 4
print("Printing values from 1 to 4")
for value in range(1, 5):
	print(value)

#range function - print 1 to 6
print("Printing values from 1 to 5")
for value in range(1, 6):
	print(value)

#making list with range
numbers = list(range(1,6))	#[1, 2, 3, 4, 5]
print(numbers)

#skipping numbers in a range
even_numbers = list(range(2, 11, 2))	#[2, 4, 6, 8, 10]
print(even_numbers)

#list of first 10 square numbers
squares = []
for num in range(1, 11):
	square = num ** 2
	squares.append(square)
print(squares)

#list of first 10 square numbers - concise version
squares_2 = []
for num in range(1, 11):
	squares_2.append(num ** 2)
print(squares_2)

#min max sum
digits = list(range(0, 10))
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))