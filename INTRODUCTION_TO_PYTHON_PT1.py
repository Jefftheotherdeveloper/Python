#This is a program that goes over the basics of Python in stages with examples

#To generate an output in the terminal you need to use "print()"
print()

#--------------------------------------------------------------------------------------------

#What is a Variable(s)
#Variable(s) is a container(s) for a value(s) (strings, integers, floats, booleans). They are meant
#to represent real life object to be given a value. In this example, height is your variable, and
#we gave it a value to store (1.19)
Height = 1.19
Weight = 68.7
bmi = Weight / Height ** 2
print(bmi)
#We lastly made a new variable called "bmi" to store both our height and weight variables as one
# which allows us to reuse those variables throughout the program which helps prevents mistakes.

#- Different types of Variables -
#Strings: To represent that your object is text, you need to write your object inside of "" or ''
first_Name = "Bob"
last_Name = "Smith"
print(first_Name)

#Integers: We use integers to represent whole numbers, you do not need any quotation marks
age = 25
quantity = 3
print(age)

#Float: Use float when your numbers will have any decimals
gpa = 3.8
price = 9.99
print(gpa)

#Boolean: They represent yes or no through "true or false", make sure the "T" or "F" is capitalised
human = True
robot = False
print(human)

#Type functions
#All numbers and strings have a specific type. You can use the "type function" to check your
#variable's value by writing "type(...)" and putting your variable inside the parentheses. Lastly
#using different types may have different behaviors. If you want your type to show in the terminal,
#then you must write your "type(...)" inside a "print()" function
float_Example = "Hello World!"
print(type(float_Example))

#To use your variables along with texts or more variables, you will need to use a "f string"
#Example: print(f"... {}") --> your variable(s) must be inside the curly brackets
#Examples using the 4 main variables
print(f"Hello {first_Name} {last_Name}")
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