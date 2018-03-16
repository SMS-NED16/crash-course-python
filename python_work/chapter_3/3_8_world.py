#Create list of places you want to visit
places = ['Florence', 'London', 'San Francisco', 'Tokyo', 'Home']

#Print list in original order
print(places)

#Use sorted() to print list in alphabetical order w/o changing original order
print(sorted(places))

#Show places is unchanged after sorted
print(places)

#reverse to change order of list
places.reverse()
print(places)

#reverse to revert to original order
places.reverse()
print(places)

#sort to alphabetical order
places.sort()
print(places)

#sort in reverse alphabetical order
places.sort(reverse = True)
print(places)