#Creating a function to make car using at least 2 fixed parameters
def make_car(manufacturer, model, **details):
	car_profile = {}
	car_profile['manufacturer'] = manufacturer
	car_profile['model'] = model
	if details:
		for key, value in details.items():
			car_profile[key] = value
	return car_profile

#Creating Accord with call to make_car
accord = make_car('honda', 'accord',
				cc = 1800, 
				seats = 4,
				condition = 'new',
				color = 'red',
				tow_package = 'True')

print(accord)

#Creating outback with call to make_car
outback = make_car('subaru', 'outback',
					color = 'blue',
					tow_package = True)
print(outback)