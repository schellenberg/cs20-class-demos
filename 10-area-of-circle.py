# Area of Circle Calculator
# Dan Schellenberg
# May 19, 2021

import math

# get user input (radius)
radius = input("What is the radius of the circle? ")

# convert data types
radius = float(radius)

# calculate
area = math.pi * radius ** 2

# output result
print("The area of the circle is", area)