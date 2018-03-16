#sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()	#sort in alphabetical order - changes original list permanently
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)	#sort in REVERSE alphabetical order
print(cars)

#sorting a list temporarily - sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:\t' + str(cars))
print('\nHere is the sorted list:\t' + str(sorted(cars)))
print('\nHere is the original list again:\t' + str(cars))

#printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()	#reverses order of elements in list
print(cars)
cars.reverse()	#changing back to original order
print(cars)

#finding length of a list
print(len(cars))