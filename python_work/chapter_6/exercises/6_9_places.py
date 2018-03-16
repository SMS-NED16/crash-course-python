#making dictionary of people and their favourite places
favourite_places = {
	'saad' : ['karachi', 'london'],
	'mashkoor' : ['lahore', 'dhaka', 'karachi', 'taxilla'],
	'nasreen' : ['home', 'karachi']
}

for name, places in favourite_places.items():
	print(name.title() + "'s favourite places")
	for place in places:
		print(place.title(), end = " ")
	print("\n")