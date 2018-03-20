def show_magicians(magicians_list):
	if magicians_list:
		for magician in magicians_list:
			print(magician.title())
	else:
		print("No magicians in list!")

performers = ['David Copperfield', 'David Blaine', 'Cris Angel',
	'Raman Sharma', 'The Great Fussili']

show_magicians(performers)