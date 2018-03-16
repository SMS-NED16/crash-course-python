#a list of dictionaries
print("List of dictionaries".upper())
alien_0 = { 'color' : 'green', 'points' : 5}	#alien 0 properties
alien_1 = { 'color' : 'yellow', 'points': 10}	#alien 1 properties
alien_2 = { 'color' : 'red', 'points' : 15}		#alien 2 properties

#create a list of all aliens on the game board
aliens = [alien_0, alien_1, alien_2]

#print each alien object/dictionary in list of aliens on board
for alien in aliens:
	print(alien)


#aliens - a more practical example
print("\nGenerating list of aliens".upper())
aliens = []		#Make an empty list for storing aliens
for alien_number in range(30):
	new_alien =  {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)	

#Show the first 5 aliens
for alien in aliens[:5]:
	print(alien)

#Show how many aliens we've created
print("Total number of aliens: " + str(len(aliens)))

#Modifying the first three aliens
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

print("\nModified the first three aliens.".upper())
for alien in aliens[:5]:
	print(alien)