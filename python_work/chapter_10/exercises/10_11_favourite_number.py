import json

favourite_number = input("What's your favourite number? ")
filename = 'fav_num.json'
with open(filename, 'w') as f_obj:
	json.dump(favourite_number, f_obj)

