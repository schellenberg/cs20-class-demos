# Area of a Circle Calculator
# Dan Schellenberg
# Nov 25, 2021

import math

# get info
radius = input('What is the radius?')

# convert to number
radius = float(radius)

# convert and output info
area = math.pi * radius ** 2
print("The area of the circle is " + str(area))