def build_profile(first_name, last_name, **details):
	#Create empty dictionary to store user details
	profile = {}

	#Add first name and last name to dictionary
	profile['first name'] = first_name
	profile['last name'] = last_name

	#Add every key value pair in details dictionary
	for key, value in details.items():
		profile[key] = value

	#return final profile
	return profile

#Function call
saad = build_profile('saad', 'siddiqui',
					age = 21,
					university = 'NEDUET',
					hobbies = ['programming', 'music'],
					favourite_animal = 'cats',
					favourite_artists = ['AC/DC', 'GNR', 'Joji'])

#Print profile as neatly formatted string
for key, value in saad.items():
	print(key.title() + ": " + str(value).title())