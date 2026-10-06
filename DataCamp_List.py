#Python List
#It is inconvenient to create multiple variables. Instead, we should use a "list []" to
#store information and data together. We are also able to apply rhem to references using a "="
#symbol after the variable's name.
family = [1.73, 1.68, 1.71, 1.89]

#Lists can also different types of variables within it too.
fam1 = ['liv', 1.73, 'Emma', 1.68, 'Mom', 1.71, 'Dad', 1.89]
#You are able to put lists inside of lists too which tells Python that these sublists
#are the elements of another list
fam2 = [['liv', 1.73],
        ['Emma', 1.68],
        ['Mom', 1.71],
        ['Dad', 1.89]]
print(fam2)

#List type
#When you write "type(...)" and put your list name inside the parameters, you can see
#theses are lists
type(fam1)

#--------------------------------------------------------------------------------------------
#Exercise
#You can group other variables within the list
a = 'is'
b = 'nice'
my_list = ['my', 'list', a, b]

#Create a area list
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.59
area_list = ['Hallway: ', hall, 'Kitchen: ', kit, 'Living room:', liv, 'Bedroom', bed, 'Bathroom', bath]
print(area_list)
#--------------------------------------------------------------------------------------------