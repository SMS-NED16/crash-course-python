from collections import OrderedDict

#Create OrderedDict object to store word-meaning pairs
glossary = OrderedDict()

#Adding word-meaning pairs to glossary
glossary['python'] = "A general purpose, versatile, high level programming language."
glossary['variable'] = "A piece of information/data stored for use in a programme."
glossary['function'] = "A block of code that performs a single, well-defined task."
glossary['list'] = "A mutable, ordered collection of variables of the same type."
glossary['tuple'] = "An immutable, ordered collection of variables of the same type."
glossary['dictionary'] = "A mutable, unordered collection of key-value pairs."

#printing word-meaning pairs in glossary
for word, meaning in glossary.items():
	print(word.upper())
	print(meaning)
	for char in range(0, len(meaning)):
		print("-", end = "")
	print()
