#making a dictionary of cities as key values
#each city has a dictionary of information about it
cities = {
	'karachi' : {
		'country' : 'pakistan',
		'population' : 100,
		'fact' : "Pakistan's largest and most densely populated city."
	},
	'lahore' : {
		'country' : 'pakistan',
		'population' : 50,
		'fact' : "Capital of Punjab. Formerly a seat of Mughal power."
	},
	'islamabad' : {
		'country' : 'pakistan',
		'population' : 10,
		'fact' : "Pakistan's capital city and home to Parliament House."
	}
}

#Printing details about each city
for city, details in cities.items():
	print(city.upper())
	print("\tCountry: " + details['country'].title())
	print("\tPopulation (millions): " + str(details['population']))
	print("\tFact: " + details['fact'])