guest_list = ['Faiq', 'Waleed', 'Haseeb', 'Najam']
print(guest_list)
print(guest_list[0] + ", I'd like you to come to dinner.")
print('Hey, ' + guest_list[1] + '! Would you like to come to dinner?')
print(guest_list[2], " let's meet for dinner tomorrow.")
print(guest_list[3], ", will you be able to come to dinner tomorrow?")

#Print name of guest who can't make it
print('Uh oh! It looks like ' + guest_list[2] + " won't be joining us for dinner.")
new_guest = 'Umer'			#storing new guest name in variable
print("I'll invite " + new_guest + " instead.")	#using this variable
print('Old Guest List:\t' + str(guest_list))	#printing original list
del guest_list[2]	#index known so using del
guest_list.insert(2, new_guest)		#index known so using insert
print("New Guest List:\t" + str(guest_list))	#printing new list

#printing messages for the guest list again
print(guest_list[0] + ", I'd like you to come to dinner.")
print('Hey, ' + guest_list[1] + '! Would you like to come to dinner?')
print(guest_list[2] + ", let's meet for dinner tomorrow.")
print(guest_list[3] + ", will you be able to come to dinner tomorrow?")


########################3.6 BEGINS HERE#######################
print("Guys, I found a bigger table, so I'm inviting more guests.")
guest_1 = "Moiz"
guest_2 = "Taqi"
guest_3 = "Fawad"
guest_list.insert(0, guest_1)	#Inserting moiz at beginning of list
middle_index = int(len(guest_list) / 2)
print(guest_list)
print(middle_index)
guest_list.insert(middle_index, guest_2)	#inserting taqi at middle
print(guest_list)
guest_list.append(guest_3)
print(guest_list)
print("PRINTING INVITATIONS USING FOR LOOP")
for person in guest_list:
	print("Hi, " + person + "! Would you like to join me for dinner tomorrow?")


########################3.6 BEGINS HERE#######################
print('\n\n3.7 BEGINS HERE - SHRINKING GUEST LIST')
print("Sorry, guys! We don't have space for " + str(len(guest_list))
	+ " people. Only for 2.")
#popping the last 5 items from list and printing message
for i in range(0, 5):
	guest_removed = guest_list.pop()
	print("Sorry, " + guest_removed + ". :(")

print(guest_list)
del guest_list[0]
print(guest_list)
del guest_list[0]	#now index of last item is 0
print('Guest list at end of programme:\t' + str(guest_list))













