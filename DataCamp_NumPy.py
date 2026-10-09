#DataCamp: "Data Analyst in Python" Course
#Topic: NumPy

#Python has no idea how to do calculations with lists. You can solve them by going through
#each list element one after the other but that is every inefficient and tiresome to write.
#but using packages like "NumPy" provides an alternative.

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [64.5, 59.2, 63.6, 88.4, 68.7]

import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)
bmi =  np_weight / np_height ** 2
print(bmi)

#You still need to pay attention because NumPy only assumes that your NumPy array can only
#contain values of a single type. If you try to create an array with different data types,
#then other data types will convert to strings. They also behave differently then your normal
#methods. Different types = different behavior.

# - Example -
#This action will just add two list together
python_list = [1, 2, 3]
print(python_list + python_list)
#This action will cause the list elements to added together
np_array = [1, 2, 3]
print(np_array + np_array)

#You can work with NumPy the same way you can with regular lists.
print(bmi[1])
print(bmi > 23) #   --> this prints out NumPy array containing booleans that matchings with
                #       each element's index
print(bmi[bmi > 23])   # --> this will print out the actual element from a subsetting list

#--------------------------------------------------------------------------------------------
#Exercise

#Create a numpy array for baseball player's height and then print out the array, the 3rd element,
#and a range from the 2nd element to the 4th
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print(np_baseball)
print(np_baseball[2])
print(np_baseball[1:4])


#--------------------------------------------------------------------------------------------