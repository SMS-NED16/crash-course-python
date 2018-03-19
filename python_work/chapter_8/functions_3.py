def get_formatted_name(first_name, last_name):
	"""Return full name, neatly formatted"""
	full_name = first_name.title() + " " + last_name.title()
	return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#optional arguments
def get_formatted_name_1(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name_1('jimi', 'hendrix')
print(musician)
musician = get_formatted_name_1('john', 'hooker', 'lee')	#first, last, middle
print(musician)


