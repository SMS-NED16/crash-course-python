#make empty list
usernames_2 = []
if usernames_2:
	if name == 'admin':
		print("Hello, admin! Would you like to see a status report?")
	else:
		print("Hello, " + name + ". Thank you for logging in.")
else:
	print("We need to find some users!")
