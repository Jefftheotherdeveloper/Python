#DataCamp: "Data Analyst in Python" Course
#Topic: Manipulating Lists

#List manipulation is ways to change elements in your list. To add or remove elements from
#your list too. To change an element, you need to use the square bracket from subsetting lists
#and then assign it a new element using the equal sign
fam = ['liv', 1.73, 'Emma', 1.68, 'Mom', 1.71, 'Dad', 1.89]
fam[7] = 1.70
print(fam)

#If you want to check what is an element's index, you can use the ".index" function and then write
#your element
print(fam.index('Dad'))

#You can even change an entire list slice at once too. You just need to get the range and
#assign the new elements within brackets.
fam[0][2] = ['lisa', 1.90]
print(fam)

# - Adding or Removing -
#The plus(+) or subtract(-) operators are different for lists but simple to use abd understand.

#Using the plus sign on a list will simply paste the two lists together.
fam + ['me', 1.95]
print(fam)
#You can also store this new list in a variable
fam_ext = fam + ['me', 1.95]
print(fam_ext)
#To remove an element from the list, you need to use "del" but remember that all the elements
#will move cover by 1 index.
del fam[2]
print(2)

#Creating a new list, you are storing a list in your computer's memory and store that address of
#that list. This means your list does not actually contain all the list elements but a reference
#to it. This becomes important when your copying lists.
x = ['a', 'b', 'c']
y = x
y[1] = 'z'
print(y)
print(x)
#When you check "x" now, you can see that the 2nd element also changed because you had copied
#the reference to the list since you made "x" equal to "y" and both of them points to the list.
#To create a list that points to a new list in the memory, you will need to use the list function.
y = list(x)

#--------------------------------------------------------------------------------------------
#Exercise

area_list = ['Hallway: ', 11.25, 'Kitchen: ', 18.0 , 'Living room: ', 20.0, 'Bedroom: ', 10.75, 'Bathroom: ', 9.50]
#Change bathroom to be 10.50 instead of 9.50 using negative indexing
area_list[-1] = 10.50
#Change "Living room" to "chill zone"
area_list[4] = 'Chill zone: '
print(area_list)

area_list = ['Hallway: ', 11.25, 'Kitchen: ', 18.0 , 'Chill zone: ', 20.0, 'Bedroom: ', 10.75, 'Bathroom: ', 10.50]
#Use the "+" operator paste "poolhouse, 24.5" to the end of the list
area1 = area_list + ['Poolhouse', 24.50]
#Extend area1 by data to the list "garage, 15.45"
area2 = area1 + ['Garage', 15.45]
#Remove "Poolhouse, 24.50" from the list and print out the updated list
print(area_list.index('Poolhouse'))
del area_list[10]
del area_list[10]
print(area_list)

#Create a variable called "area_copy" that is an explicit copy of areas that doesn't affect areas.
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
print(areas_copy)
#--------------------------------------------------------------------------------------------