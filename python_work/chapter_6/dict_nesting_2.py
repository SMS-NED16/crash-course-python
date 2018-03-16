#Store information about pizza being ordered
pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'extra cheese']
}

#Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza with " +
	"the following toppings:")
for topping in pizza['toppings']:
	print(topping.title(), end = ", ")
print()

#Store a list of favourite programming languages for each person
favourite_languages = {
	'sarah' : ['python'],
	'john' : ['java', 'python', 'ruby'],
	'phil' : ['golang', 'ruby', 'python', 'c', 'c++'],
	'edward' : ['ruby', 'haskell']
}

for name, responses in favourite_languages.items():
	if(len(responses) > 1):
		print(name.title() +"'s favourite languages are:")
	else:
		print(name.title() + "'s favourite language is: ")
	for language in responses:
		print("\t" + language.title())