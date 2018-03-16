#Forgetting to indent - part 1

"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)				#missing indentation - IndentationError - expected an Indented block
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title())
print("I can't wait to see your next trick, " + magician.title() + "!")
#last value stored in magician is the value at end of list - caroline

"""
message = "Hello Python World"
	print(message)		#indentation error - unexpected indent
"""

message = "Hello Python World"
print(message)

#Unnecessary indentation after loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	#should be unindented - will now print for EACH element in magicians
	print("Thank you everyone, that was a great magic show!")


#forgetting the colon
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians
	print(magician)	#invalid syntax error
"""
