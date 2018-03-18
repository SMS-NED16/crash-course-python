#list of active sandwich orders - will be filtered to remove pastrami
sandwich_orders = ['chicken', 'mayo', 'egg', 'ham', 'pastrami',
 'chicken', 'pastrami', 'mayo', 'pastrami', 'pastrami']

#list to hold finished orders
finished_sandwiches = []

#let user know that the deli is out of pastrami
print("Sorry! We're all out of pastrami!")

#removing all active pastrami orders
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

#add remaining orders to finished_sandwiches one by one
while sandwich_orders:
	current_order = sandwich_orders.pop()
	print("Prepaing a " + current_order.title() + " sandwich.")
	print("...")
	print("Done!")
	finished_sandwiches.append(current_order)

#Echo list of finished orders
for sandwich in finished_sandwiches:
	print(sandwich.title() + " sandwich is ready!")