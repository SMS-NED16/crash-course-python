def city_country(name, country):
	details = "\"" + name.title() + ", " + country.title() + "\""
	return details

print(city_country("karachi", "pakistan"))
print(city_country("london", "united kingdom"))
print(city_country("tokyo", "japan"))