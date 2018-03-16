#making list of friends
friends = ["Faiq", "Haseeb", "Waleed", "Najam", "Moiz", "Rameez"]


#print first three items in list
print("The first three items in the list are: " + 
	str(friends[:3]))

#print the middle three items in the list
middle_index = int(len(friends)/2)

print("The middle three items in the list are: " + 
	str(friends[middle_index - 1: middle_index + 2]))


#print the last three items in the list
print("The last three items in the list are: " + 
	str(friends[-3:]))
