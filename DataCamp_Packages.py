#DataCamp: "Data Analyst in Python" Course
#Topic: Packages

#Packages can be as a directory of Python scripts. Each script is a so-called module where the
#module specify the functions, methods, and types aimed to solve particular problems. There
#are thousands of packages available to use. To use packages, you will need to install them
#into your Python system and then use code to tell Python you want to use these packages. Make
#sure to import your packages using an import statement. You can refer packages to have a
#different name instead of using the package's name, this is a preference.

import numpy as np
np.array([1,2,3])
print(np.array([1,2,3]))

#There are cases when you only want to use a specific function from a package, so Python allows
#you to make this explicit in your code by using "from _package's name_ import _function's name_".
from numpy import array
array([4,5,6])
#But when your writing with a large amounts of code, it can because easy to forget if you are
#using a function from a package. So the standard practice is to import the fully package and
#give it a name.

#There maybe situations where you want to use a function that is part of a subpackage of a
#package. You will need to write this statement:
#"from _package.subpackage_ import _function's name_ as _created name_"
#Example: from scipy.linalg import inv as my_inv

#--------------------------------------------------------------------------------------------
#Exercise

#For the sake of space in my computer. I won't download anymore packages but will still
#write out the code as comments for examples to look back at.

#import math
#C = 2 * 0.43 * math.pi
#A = pi * 0.43 ** 2
#print(Circumference: + str(C))
#print("Area: " + str(A))

#--------------------------------------------------------------------------------------------