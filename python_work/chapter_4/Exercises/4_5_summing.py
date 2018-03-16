#make a list from 1 to 1M
one_to_million = [val for val in range(1, 1000001)]

#sum all numbers and store result
sum_of_numbers = sum(one_to_million)
minimum = min(one_to_million)
maximum = max(one_to_million)

#print sum
print("Sum of numbers from 1 to 1M:\t" + str(sum_of_numbers))
print("Minimum value:\t" + str(minimum))	#should be 1
print("Maximum value:\t" + str(maximum))	#should be 1000000
