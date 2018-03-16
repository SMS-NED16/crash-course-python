#list of current users
current_users = ['saad', 'mashkoor', 'admin', 's1234', 'smash_sid']

#list of new users
new_users = ['abc', 'xyz', 'pqr', 'saad']

#loop through new users
if new_users:			#if new_users is not empty
	for user in new_users:	#for every username in new_user
		#check if same combination of chars is used by current_user (case-insensitive)
		if user.lower() in current_users:	
			print("Username " + user + " is not available.")
			print("Please select another username.")
		else:
			print("Username " + user + " is available.")
else:					#no new users to check
	print("No more new users!")