"""
Counts the number of words in Alice In Wonderland
by reading the text file alice.txt
Also demonstrates try/except/else concept
"""

def count_words(filename):
	"""Count the apprixmate number of words in a file"""
	try:
		with open(filename, encoding="utf-8") as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " dos not exist."
		print(msg)
	except UnicodeDecodeError:
		print("Cannot convert unicode to string.")
	else:
		# Count the approximate number of words in the file
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words)
			+ " words.")

def count_words_pass(filename):
	"""
	Count the approximate number of words in a file
	But print no error message in case of exceptions
	"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	except UnicodeDecodeError:
		pass
	else:
		#Count the approximate number of words using split
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + 
			str(num_words) + " words.")


#creating list of files to read
print("Exception handling with error messages".upper())
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little-women.txt']
for filename in filenames:
	filename = "text_files/" + filename
	count_words(filename)

print("\nException handling without error messages".upper())
for filename in filenames:
	filename = "text_files/" + filename
	count_words_pass(filename)


