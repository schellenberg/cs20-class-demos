# Write a program that will compute the area of a circle.
# Prompt the user to enter the radius and print a nice
# message back to the user with the answer.

import math

#get info
radius = input("What's the radius? ")

#convert data type
radius = int(radius)

#do math
area = math.pi * radius ** 2

#print message
#print("The area of the circle is " + str(area))

#nicer way to show message
print(f"The area of the circle is {area}")
