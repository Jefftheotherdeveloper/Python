#DataCamp: "Data Analyst in Python" Course
#Topic: Functions

#A function is a reusable piece of code, aimed at solving a particular task. You can call
#on functions instead of writing the code yourself. These are built in code that your
#programming languages allows you to use. When using functions, you need to pass your
#variable's name through the parentheses. Normally, it's not important to know what the
#code for the functions are.

# - Examples of functions -
#   -> "max()"
#Gives you the biggest number in your list
fam_height = [1.73, 1.68, 1.71, 1.89]
max(fam_height)
#It is possible to assign the results of a function call to a new variable
tallest = max(fam_height)
print(tallest)

#   -> "round()"
#This takes 2 input: the number you want to round and the second by how many digits after the
#decimal point you want to keep.
round(1.68, 1)

#   -> "help()"
#Opens documentation on functions you would like to know more about when you write the function
#inside the parentheses.
help(round)

#--------------------------------------------------------------------------------------------
#Exercise

var1 = [1,2,3,4]
var2 = True
#Print out the type of var1 using "type()" function
print(type(var1))
#Print out the length of var1 using "len()" function
print(len(var1))
#Covert var2 into an integer using "int()" function
output = int(var2)


first = [11.25, 18, 20]
second = [10.75, 9.50]
#Merge the context of the first and second list together
full = first + second
#Find out what "sorted()" does and call it for full and make the reverse argument to be True
help(full)
fully_sorted = sorted(full, reverse = True)
print(fully_sorted)
#--------------------------------------------------------------------------------------------