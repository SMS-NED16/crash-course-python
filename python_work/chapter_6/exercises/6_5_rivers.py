#making dictionary of rivers and their countries
rivers = {
	'indus' : 'pakistan',
	'ganges' : 'india',
	'nile' : 'egypt'
}

#Print a sentence about each river
print("Print a sentence about each river".upper())
for river, country in rivers.items():
	print("The " + river.title() + " runs through " +
	 country.title() + ".")

#Use a loop to print name of each river in dictionary
print("\nPrinting name of each river in dictionary".upper())
for river in rivers:
	print(river.title())

#Use a loop to print name of each country in dictionary
print("\nPrinting name of each country in dictionary".upper())
for country in rivers.values():
	print(country.title())

#Alternatively
print("\nPrinting countries without using values function".upper())
for value in rivers:
	print(rivers[value].title())