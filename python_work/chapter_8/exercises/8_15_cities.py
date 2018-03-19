def describe_city(name, country = 'Pakistan'):
	print(name.title() + " is a city in " + country.title() + ".")

describe_city('karachi')
describe_city('lahore')
describe_city('islamabad')
describe_city('london', 'united kingdom')
describe_city(country = 'iceland', name  = 'reykjavik')