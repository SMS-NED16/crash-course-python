def sandwiches(*ingredients):
	for item in ingredients:
		print("Adding " + item + " to your sandwich.")
	print("Done! Your sandwich contains:", end = " ")
	for item in ingredients:
		print(item, end = ", ")
	print("\n\n")

sandwiches('egg', 'mayo')
sandwiches('egg', 'mayo', 'grilled chicken')
sandwiches('cheese', 'tomatoes')