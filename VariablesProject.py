#Variables = A container for a value (string integer, float, boolean)

#Strings
#To represent that your object will be a string, you need to write your object inside of "" or ''
first_name = "Bob"
last_name = "Smith"
print(first_name)

#Integers
#Using integers are for whole numbers, you do not need any quotation marks
age = 25
quantity = 3
print(age)

#Float
#Use float when your numbers will have any decimals
gpa = 3.8
price = 9.99
print(gpa)

#Boolean
#Meant for "true or false", make sure the "T" or "F" is capitalised
human = True
robot = False
print(human)

#To use your variables along with texts or more variables, you will need to use a "f string"
#Example: print(f" {}") --> your variable(s) must be inside the curly brackets
#Examples using the 4 main variables
print(f"Hello {first_name} {last_name}")
print(f"You are {age} years old!")
print(f"The total price is ${price}")
print(f"Human status: {human}")

#--------------------------------------------------------------------------------------------
#Easy program to demonstrate how all the variables can be used together
#This program will be based on a car's information if it belonged to a car dealership
print("----------------------")
car_Brand = "Ford"
car_Model = "F-150"
car_Year = 2026
car_Price = 38809.99
car_Forsale = True

print("|=-=-=-=-=-=|")
print(f"Car: {car_Brand} {car_Model} {car_Year}")
print(f"Price: ${car_Price}")
print(f"Available for sell: {car_Forsale}")
print("|=-=-=-=-=-=|")

print("----------------------")