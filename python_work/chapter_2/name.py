#Basic string manipulation
name = "ada lovelace"
print(name.title())			#First letter of each word is capitalised
print(name.upper())			#ALL letters are capitalised
print(name.lower())			#ALL letters are converted to lowercase

"""String concatentation"""
first_name = "ada"
last_name = "lovelace"
full_name = (first_name + " " + last_name)

"""
Concatenating string variables to output a proper message
First, convert full_name variable to title() i.e. all first letters capitalised
Then, concatenate this with "Hello, " on the left and "!" on the right
"""
print("Hello, " + full_name.title() + "!")

#Concatenation for storing messages in variable
message = "Hello, " + full_name.title() + "!"
print(message)

"""Using whitespace"""
print("Python")
print("\nPython")	#\n means new line
print("\tPython")	#\t means tab - 4 to 8 spaces
print("Languages:\n\tPython\n\tC\n\tJavaScript")	#combining \n and \t

"""Stripping Whitespace"""
favourite_language = "python "		#has whitespace on the right
print(favourite_language)			#print 'python '
favourite_language.rstrip()			#remove whitespace on RIGHT
print(favourite_language)			#print 'python ' - temporary rstip

#Stripping whitespace and reassigning the value to the variable
favourite_language = favourite_language.rstrip()
print(favourite_language);

#Stripping whitespace from the left side of the string
new_language = " Go lang "
print(new_language)
new_language = new_language.rstrip()	
new_language = new_language.lstrip()
print(new_language)