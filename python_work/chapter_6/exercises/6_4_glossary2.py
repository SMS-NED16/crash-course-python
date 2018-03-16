#creating glossary of common Python terms
glossary = {
	'python' : 'A general purpose, high-level programming language',
	'variable' : 'A piece of information or data used by a programme',
	'list' : 'A mutable collection of variables/values of the same data type',
	'tuple' : 'An immutable collection of variables/values of the same data type',
	'mutable' : 'A value is said to be mutable if it can be reassigned'
}

#Looping through dictionary
for term, meaning in glossary.items():
	print(term.upper())
	print(meaning)
	for num in range(0, len(meaning)):
		print("=", end = "")
	print()

#Adding five more terms to the dictionary
print("Adding 5 more terms to the dictionary.".upper())
glossary['dictionary'] = 'A collection of key-value pairs'
glossary['conditional'] = 'An expression that evaluates to True of False'
glossary['string'] = 'A fundamental data type in Python used to store a sequence of characters'
glossary['immutable'] = 'A variable is said to be immutable if it cannot be reassinged'
glossary['PEP8'] = 'Python Enhancement Proposal 8'

#looping through dictionary again
print("\nPrinting updated dictionary".upper())
for term, meaning in glossary.items():
	print(term.upper())
	print(meaning)
	for num in range(0, len(meaning)):
		print("=", end = "")
	print()