#DataCamp: "Data Analyst in Python" Course
#Topic: Methods

#Methods are functions that belong to objects. Everything in Python is an object, they have specific
#methods associated with them depending on the data type. Remember that depending the type of the object,
#the method behave differently. When calling methods, you need to write your variable's name followed
#with a dot "." and then the method with parenthesis. Lastly, place an element inside if you need to.

#You can use the count method to count how many times an elements appears on a list. ".count()"
fam = ['liv', 1.73, 'Emma', 1.68, 'Mom', 1.71, 'Dad', 1.89]
print(fam.count(1.73))

# - Examples of Methods -
#Capitalizes the first letter of the string ".capitalize()"
sister = 'liz'
sister.capitalize()
print(sister)
#Replaces any parts in a string with something else ".replace()"
sister.replace('z', 'sa')
print(sister)

#Some methods can change the object they are called on. Like the append method ".append()"
fam.append('me')
fam.append(2.01)
print(fam)
#We can see that the list has been updated and now includes a new string and float. But some
#methods don't change the object they are called on.

#--------------------------------------------------------------------------------------------
#Exercise

place = 'poolhouse'
#Covert poolhouse to upper case using the ".upper()" method and store it in a new variable
place_up = place.upper()
print(place)
print(place_up)
#Print the number of "o" in place by using ".count()"
print(place.count('o'))

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
#Print out the index of 20.0 and how many times 9.50 appears
print(areas.index(20.0))
print(areas.count(9.50))
#Use append to add a poolhouse and garage sizes to the list, then reverse the list and print
#out the updated list
areas.append(24.50)
areas.append(15.45)
areas.reverse()
print(areas)
#--------------------------------------------------------------------------------------------