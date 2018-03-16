#create new dictionary
user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi'
}	

print(user_0)	#prints dictionary as a string 

#print individual k-v pairs using items()
print("PRINTING WITH key-value")
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

#can use any variable names for key-value such as k-v
print("PRINTING WITH K-V")
for k, v in user_0.items():		
	print("\nKey: " + k)
	print("Value: " + v)

#Dictionaries with the same key-value format for all items
print("\nFAVOURITE LANGUAGES")
favourite_languages = {
	'jen' : 'c',
	'sarah' : 'python',
	'edward' : 'ruby',
	'phil' : 'python'
}

for person, language in favourite_languages.items():
	print(person.title() + "'s favourite language is " +
		language.title() + ".")

#Looping through keys only
print("\nWORKING WITH KEYS")
for name in favourite_languages.keys():
	print(name.title())
print("\nFor name in favourite_languages")

for item in favourite_languages:
	print(item.title())

for item in favourite_languages:
	print(favourite_languages[item].title())

#Accessing values in a for loop
print("\nFRIENDS AND LANGUAGES DICTIONARIES")
friends = [ 'phil', 'sarah']
for name in favourite_languages.keys():
	print(name.title())
	if name in friends:
		print("Hi, " + name.title() +
			", I see your favourite language is " + 
			favourite_languages[name].title() + "!")

#FINDING SPECIFIC KEYS IN DICTIONARIES
print("\nFinding specific keys in dictionaries".upper())
if 'erin' not in favourite_languages.keys():
	print("Erin, please take our poll!")


#SORTING KEYS
print("\nPrinting keys in a specific order with sorted()".upper())
favourite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
}

#temp copy of languages.keys() list is sorted 
for name in sorted(favourite_languages.keys()):	
	print(name.title() + ", thank you for taking the poll.")


#Looping through values
print("\nLooping through all values - values()".upper())
for value in favourite_languages.values():
	print(value.title(), end = " ")
print()

#Using sets - a set contains unique values - no repeated vals
print("\nLooping through all values - SET".upper())
for value in set(favourite_languages.values()):
	print(value.title(), end = " ")
