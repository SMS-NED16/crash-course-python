import json

#First try and see if fav_num.json file present in directory
try:
	with open('fav_num.json') as f_obj:
		fav_num = json.load(f_obj)

#if the fav_num.json file is not present, user has not entered fav number
except FileNotFoundError:
	number = input("What is your favourite number?")
	with open('fav_num.json', 'w') as f_obj:
		json.dump(number, f_obj)
		print("Will remember your favourite number!")
#If file is present, read its data and output fav number to the screen
else:
	print("Your favourite number is " + str(fav_num) + ".")