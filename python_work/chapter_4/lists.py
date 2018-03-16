magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

cats = ['Scottish Fold', 'Tabby', 'Maine Coon']
for cat in cats:
	print(cat)

dogs = ['Labrador', 'Retreiver', 'Corgi']
for dog in dogs:
	print(dog)

print()
#Using values in for loops
for magician in magicians:
	print(magician.title() + ", that was a great trick!")

print()
#multiple values in for loops
for magician in magicians:
	print('Current Magician:\t' + magician.title())
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title())
	print()
print("Thank you, everyone. That was a great magic show!")
