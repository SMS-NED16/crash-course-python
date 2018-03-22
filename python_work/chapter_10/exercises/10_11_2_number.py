import json

#try opening the fav_num.json file and reading input
try:
	with open('fav_num.json') as f_obj:
		num = json.load(f_obj)
except FileNotFoundError:
	print("No file called fav_num.json")
else:
	print("Your favourite number is " + str(num) + ".")