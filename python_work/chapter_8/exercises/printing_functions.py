def print_models(models_to_print, printed_models):
	"""Pops every item in list models_to_print and appends to printed_models"""
	while models_to_print:
		for model in models_to_print:
			current_model = models_to_print.pop()
			print("Currently printing " + current_model + ".")
			printed_models.append(current_model)

def print_list(my_list):
	"""Prints every item in list on separate line"""
	for item in my_list:
		print(item.title())
