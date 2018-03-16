#make list of usernames
usernames = ['abcd', 'saad12', 'SugoiSenpai', 'M_hassan', 'admin']

#loop through the list of usernames
for name in usernames:
	if name == 'admin':		#different message for admin
		print("Hello, admin! Would you like to see a status report?")
	else:					#generic message for everyone else
		print("Hello, " + name + ". Thank you for logging in again!")

#make empty list
usernames_2 = []
if usernames_2:
	if name == 'admin':
		print("Hello, admin! Would you like to see a status report?")
	else:
		print("Hello, " + name + ". Thank you for logging in.")
else:
	print("We need to find some users!")
