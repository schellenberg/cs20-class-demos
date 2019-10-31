# Area of a Circle Calculator
# Dan Schellenberg
# October 8, 2019

import math

radius = input("Please enter the radius of the circle: ")
radius = float(radius)

area = math.pi * radius ** 2

print("The area of the circle is " + str(area))
