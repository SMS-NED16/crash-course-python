#dict of people and their favourite languages
favourite_languages = {
	'sarah' : 'c',
	'john' : 'python',
	'brad' : 'c++',
	'mike' : 'ruby',
	'jessica' : 'java'
}

#list of people
respondents = ['sarah', 'jessica', 'andrew', 'mike', 'gilfoyle',
				'peyton', 'joaquin', 'brad']

#parse list of names, check if they have taken the survey
for name in respondents:
	if name not in favourite_languages.keys():
		print(name.title() + ", you should take this survey.")
	else:
		print("Thank you for taking the survey, " + name.title() + ".")
print()