languages = ["English", "Urdu", "Bangla", "French", "Japanese", "Mandarin"]
print(languages)	#print for lists
print(str(languages))	#print with str typecast
print("Length of list:\t" + str(len(languages)))

#inserting a language
languages.insert(0, "Spanish")
print(languages)

#pop
removed_lang_1 = languages.pop()
print("I removed the language:\t" + removed_lang_1 + ".")
print(languages)

removed_lang_2 = languages.pop(3)
print("I removed the language:\t" + removed_lang_2 + ".")
print(languages)

#append
new_lang = "Bangla"
languages.append(new_lang)
print("After appending " + new_lang + ",:\n" + str(languages))

#del
del languages[3]
print("After del languages[3]")
print(languages)

#remove
languages.remove('Spanish')
print("After languages.remove('Spanish')")
print(languages)

#sorted
print(str(sorted(languages)))
print("Sorted function, so original unchanged")
print(languages)

#sort
languages.sort()
print(languages)

#reverse sort
languages.sort(reverse = True)
print(languages)

languages.sort()
print(languages)

#reverse
print("REVERSE")
languages.reverse()
print(languages)

#accessing last index
print(languages[-1])

