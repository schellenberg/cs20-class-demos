# Area of a Circle Calculator
# Dan Schellenberg
# Oct 16, 2023

import math

# get radius from user
radius = input("What is the radius? ")

# convert info to a number data type
radius = int(radius)

# math to calculate area
area = math.pi * radius ** 2

# round to the nearest 2 decimals
area = round(area, 2)

# print the result
print("The area of the circle is " + str(area))
