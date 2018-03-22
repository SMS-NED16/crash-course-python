def get_location(city, country, population=""):
	"""
	Returns neatly formatted string with city, country, and 
	optional popualtion"""
	details = city.title() + ", " + country.title()
	#if population is specified i.e. not default value, append
	if population:
		details += " - population " + str(population)
	#in either case, return details
	return details
