bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)	#prints list with brackets, commans, and quote marks

print(bicycles[0])	#prints first element in list - trek

print(bicycles[0].title())	#prints Trek

print(bicycles[1])	#2nd item in list
print(bicycles[3])	#4th item in list

#using reverse indexes 
print(bicycles[-1])	#prints last element in list
print(bicycles[-2])	#prints second-last element in list
print(bicycles[-3])	#prints third-last element in list

#concatenation using lists 
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)	#prints 'My first bicycle was a Trek.'

#accessing and changing elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'	#assign new value to element at index 0
print(motorcycles)			


#appending elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append("Ducati")
print(motorcycles)


#appending to empty list
m_cycles = []	#empty list
m_cycles.append('honda')
m_cycles.append('yamaha')
m_cycles.append('suzuki')
print(m_cycles)

#insert at position	
m_cycles.insert(0, 'ducati')	#insert 'ducati' @ index 0
print(m_cycles)	#ducatio, honda, yamaha, suzuki 

#remove from position - del
print(m_cycles)
del m_cycles[0]	#delete ducati - we know this is at index 0
print(m_cycles)	#honda, yamaha, suzuki
del m_cycles[2]	#suzuki 
print(m_cycles)

#remove from end - pop
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop();
print(motorcycles)	#honda, yamaha
print(popped_motorcycle)	#suzuki

#remove from any position - pop(argument)
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '  + first_owned.title() + '.')

#removing by value - remove
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

#removing using a variable as a key
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'	#variable to store value to be removed
motorcycles.remove(too_expensive)	#pass variable to remove function
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')