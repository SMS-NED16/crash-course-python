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