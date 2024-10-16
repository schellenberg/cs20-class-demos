# Area of a Circle Calculator
# Dan Schellenberg
# Oct 16, 2024

import math

# get radius from user
radius = input("What is the radius of the circle? ")

# convert to a number
radius = float(radius)

# calculate the area
area = math.pi * radius ** 2

#round to two digits
area = round(area, 2)

# print the result
print("The area is " + str(area) + " units squared.")


