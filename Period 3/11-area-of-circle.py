# Area of a Circle Calculator
# Dan Schellenberg
# Mar 18/26

import math

#get info from user
radius = input("What is the radius of the circle? ")

#convert data types
radius = float(radius)

#do the math
area = math.pi * radius ** 2
area = round(area, 2)

#print out the answer
print("The area of the circle is: " + str(area))