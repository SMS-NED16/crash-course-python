import printing_functions as pf

#Creating a list of models to print
printing_orders = ['death star', 'obi wan', 'yoda', 'stormtrooper helmet']

#Creating empty list of finished models
finished_orders = []

#Echoing results before print_models call
print("Before print_models call, the two lists are as follows.")
print("\nprinting_orders".upper())
pf.print_list(printing_orders)
print("\nfinished orders".upper())
pf.print_list(finished_orders)

#Calling print operation
print("\nCalling print_orders".upper())
pf.print_models(models_to_print=printing_orders,
		printed_models=finished_orders)

#Echoing results after print_models
print("\nAfter print_models call, the two list are as follows")
print("\nprinting_orders".upper())
pf.print_list(printing_orders)
print("\nfinished_orders".upper())
pf.print_list(finished_orders)