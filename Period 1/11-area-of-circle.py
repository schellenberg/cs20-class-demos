# Area of a Circle Calculator
# Dan Schellenberg
# Mar 18/26

import math

#get radius and convert to a number
radius = input("What's the radius of the circle? ")
radius = float(radius)

#calculate the answer and round it
area = math.pi * radius ** 2
area = round(area, 2)

# print out the answer
print("The area of the circle is: " + str(area))