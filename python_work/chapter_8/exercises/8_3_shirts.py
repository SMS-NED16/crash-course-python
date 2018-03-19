def make_shirt(size, message):
	print("Making a " + size.lower() + " shirt with message '" +
		message + "'.")

#calling function with positional arguments	
make_shirt("large", "That's Finna Woke")

#calling function with keyword arguments
make_shirt(message = "Cool Nerd Joke", size = "medium")