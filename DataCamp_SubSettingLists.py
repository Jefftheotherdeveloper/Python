#DataCamp: "Data Analyst in Python" Course
#Topic: Subsetting Lists

#To access information in an array, we need to use the index feature. The first value of an
#index starts at 0 and counts up by 1. If you want to access a specific element in your array,
#you need to count to your element. To count from 0 which will make it easier.

#Index: 0       1       2     3     4     5      6      7
fam = ['liv', 1.73, 'Emma', 1.68, 'Mom', 1.71, 'Dad', 1.89]

#To call the specific you want. You need to write your array's variable name and put square
#brackets next to it. Then write the index you want inside the brackets.
print(fam[2])

#We can use negative indexs which counts backwards from the list, but you start at -1 instead of 0
print(fam[-1])

#List slicing: the action to select multiple elements from a list which creates a new list. You
#can do this by specifying a range using a colon inside the brackets.
print(fam[3:5])
#Maybe will assume the output will be "1.68, Mom, 1.71" but it will be "1.68 and Mom" because the
#syntax allows where the index starts is included but the end is excluded. This is important to
#remember when your creating your range.

#Lastly, you can leave out a start or last index because python will know to start from 0 or
#go all the way to the end of the range/list. By leaving out one of your ranges
print(fam[:5])  # <-- Counts from the start into index 5
print(fam[3:])  # <-- Counts from index 3 into the end


#--------------------------------------------------------------------------------------------
#Exercise
area_list = ['Hallway: ', 11.25, 'Kitchen: ', 18.0 , 'Living room:', 20.0, 'Bedroom', 10.75, 'Bathroom', 9.50]

#Print out the 2nd element in the list
print(area_list[1])
#Print out the last element in the list
print(area_list[-1])
#Print out the area of the living room from the list
print(area_list[5])

#Use slicing to create downstairs (Contains first 6 elements of the last)
downstairs = area_list[0:6]
#Use slicing to create upstairs (Contains last 4 elements of the last)
upstairs = area_list[6:]
print(downstairs)
print(upstairs)

#When you are trying to subsetting lists within lists. The first index you use will look up what inner
#list your trying to access while the second index is to retrieve the element within that list
house = [['Hallway: ', 11.25]
         ['Kitchen: ', 18.0]
         ['Living room:', 20.0]
         ['Bedroom', 10.75]
         ['Bathroom', 9.50]]
#Subset the list "house" to get "9.50"
print(house[4][1])
#--------------------------------------------------------------------------------------------