def make_shirt(message = 'I love Python', size = 'large'):
	print("Making a " + size + " shirt with the message '" + message + ".")

make_shirt() #default size, default message
make_shirt(size = 'medium')	#medium size, default message
make_shirt(size = 'small', message = "That's finna woke")	

