#creating glossary of Python terms
glossary = {
	'variable' : 'A piece of data or information used by Python',
	'boolean' : 'A term used to describe a True/False variable',
	'list' : 'A mutable collection of variables of the same type',
	'tuple' : 'An immutable collection of variables of the same type',
	'dictionary' : 'A collection of key-value pairs'
}

#Printing glossary contents
if glossary:
	for key,value in glossary.items():
		print(key.upper())
		print(value)
		for i in range(0, len(value)):
			print("-", end = "")
		print()
print("End of glossary")