from car import Car

"""
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#Modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Modifying an attribute's value through a setter function
my_new_car.update_odometer(35)	
my_new_car.read_odometer()
my_new_car.update_odometer(23)	#prints warning message - invalid argument
my_new_car.read_odometer()		#odometer reading unchanged
"""

#Modifying an attribute value through an increment method
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()