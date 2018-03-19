#Positional arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#order of arguments matters when using positional arguments
#Function call below will print 
#I have a harry. My harry's name is Hamster
describe_pet('harry', 'hamster')	

#keyword arguments
describe_pet(animal_type='dog', pet_name='borko')
describe_pet(pet_name='borko', animal_type='dog')

#default values
def describe_pets_1(pet_name, animal_type = 'dog'): #dog is default value
	 """Display information about a pet"""
	 """Contains a default value for parameter 'animal_type'"""
	 print("I have a " + animal_type + ".")
	 print("My " + animal_type +"'s ame is " + pet_name.title() + ".\n")
describe_pets_1(pet_name = 'fluffy', animal_type = 'bunny')
describe_pets_1(pet_name = 'borko')

#Equivalent Function Calls
def describe_pet(pet_name, animal_type = 'dog')