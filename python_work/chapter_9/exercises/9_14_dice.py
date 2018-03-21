from random import randint

class Die():
	"""A simple class to represent a die with user-defined number of sides"""
	def __init__(self, sides = 6):
		"""Initialises number of sides to 6 unless otherwise specified"""
		self.sides = sides

	def roll_die(self, number_of_rolls):
		"""
		Prints a random number between 1 and the number of sides of the die
		"""
		for roll in range(0, number_of_rolls):
			print(str(randint(1, self.sides)), end = ", ")
		print()


#Creating instances of Die with 6, 10, and 20 sides
die_6 = Die()		#6-sided die - default side init to 6
die_10 = Die(10)	#10-sided die
die_20 = Die(20)	#20-sided die

#Rolling each die 10 times
print("rolling 6 sided die".upper())
die_6.roll_die(10)

print("\nrolling 10 sided die".upper())
die_10.roll_die(10)

print("\nrolling 20 sided die".upper())
die_20.roll_die(10)



