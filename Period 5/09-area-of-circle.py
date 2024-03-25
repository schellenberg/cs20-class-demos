# Area of a Circle Calculator
# Dan Schellenberg
# March 25, 2024

#Write a program that will compute the area of a circle.
#Prompt the user to enter the radius and
#print a nice message back to the user with the answer.

# get user input
radius = input("What's the radius? ")

# convert data types
radius = float(radius)

# do the math calculations - pi times radius squared
area = 3.14 * radius ** 2

# print the result
print("The area of the circle is " + str(area))


