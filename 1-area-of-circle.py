# Area Of Circle Calculator
# Dan Schellenberg
# Oct 8, 2019

# Write a program that will compute the area of a circle.
# Prompt the user to enter the radius and print a nice
# message back to the user with the answer.

radius = input("What is the radius of the circle? ")
radius = float(radius)

area = 3.14 * radius ** 2

print("The area of the circle is " + str(area))