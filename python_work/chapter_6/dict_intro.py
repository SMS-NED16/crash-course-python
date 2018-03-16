#Creating a dictionary to store alien color and points
alien_0 = {'color' : 'green', 'points' : 5}

#Accessing values stored in key-value pairs of alien_0
print(alien_0['color'])		#accesses value in 'color' key
print(alien_0['points'])	#accesses value in 'points' key

#Simplest dictionary will have only one key-value pair
alien_1 = {'color' : 'red'}
print(alien_1)
print(alien_1['color'])

#Accessing dictionary values
print(alien_0['color'])
print(alien_0['points'])

#Using key-value pairs - a practical example
alien_0 = {'color' : 'green', 'points' : 5}
print("You just shot down a " + alien_0['color'] + " alien.")
print("You earned " + str(alien_0['points']) + " points.")
points_earned = alien_0['points']	#store value from key-value pair in variables
print("You earned:\t" + str(points_earned) + " points.")

#adding key-value pairs to dictionaries
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
alien_0['x_position'] = 0		#add new key-value pair -> x pos = 0
alien_0['y_position'] = 25		#add new key-value pair -> y pos = 25
print(alien_0)

#starting with empty dictionaries
alien_0 = {}	#empty dictionary init with empty curly brackets
print(alien_0)
alien_0['color'] = 'green'	#init color key-value pair
print(alien_0)				#echo change
alien_0['points'] = 5		#init points key-value pair
print(alien_0)				#echo change

#modifying key values
alien_0 = {'color' : 'green', 'points' : 5}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


#modifying dictionary values - part 2
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

#Move the alien to the right
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3		#this must be a fast alien

#The new position is the old position plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

#Deleting key-value pairs
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#Dictionary to store several objects of same type	
#dictionary of four string : string key-value pairs
#in each key-value pair, key = name, value = fav lang
favourite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}
print(favourite_languages)
print("Sarah's favourite language is " +
	 str(favourite_languages['sarah']).title())
