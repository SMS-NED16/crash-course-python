"""
Counts the number of each word from a list appears in
a text downloaded from Project Gutenberg
"""

def analyse_text(filename, word_bank):
	"""
	Tries to open the file and store it as a single string in contents
	Prints error message if the file is not found
	If file found, finds occurrence of every word in word_bank in file
	"""
	try:
		with open(filename, encoding="utf-8") as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("Could not find file " + filename + ".")
	else:
		for word in word_bank:
			count = contents.lower().count(word)
			print("The word '" + word + "' appears " + str(count)
				+ " times.")

#Filepaths for two books to analyse
prejudice = "text_files/pride_and_prejudice.txt"
darkness = "text_files/heart_of_darkness.txt"

#wordbank of all words to be searched for in books
words = ['the', 'and', 'to', 'congo', 'london']

#Analysing the first book
print("Analysing 'Pride and Prejudice'".upper())
analyse_text(prejudice, words)

#Analysing the second book
print("\nAnalysing 'Heart of Darkness'".upper())
analyse_text(darkness, words)