#Typecasting = the process of converting one variable from a data type to another:
# str(), int(), float(), bool()

name = "Jeff"
age = 18
gpa = 3.5
is_student = True

#Using the type function "type(...)" allows you to get the data type of an variable or value by passing the variable
# inside the type function.
type(name)
#Just writing the type function like that will not show a output in the terminal when you run the program. You need
#to use a print statement "print(type(...))"
print(type(name))

#To convert one data type to another, you will need to reassign your variable to the data type function you want
gpa = int(gpa)
print(gpa)