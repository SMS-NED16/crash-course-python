#List to store sandwich orders
sandwich_orders = ['Pastrami', 'Cheese and Ham', 'Sundried Tomato',
 'Hot and Spicy Chicken', 'Grilled Cheese']

#List of completed/finished sandwich orders
finished_sandwiches = []

while sandwich_orders:
 	current_order = sandwich_orders.pop()
 	print("Preparing a " + current_order.title() + " sandwich.")
 	print("...")
 	print("Done!\n")
 	finished_sandwiches.append(current_order)

for sandwich in finished_sandwiches:
	print("A " + sandwich.title() + " sandwich is ready.")