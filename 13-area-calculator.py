# Area Calculator
# Dan Schellenberg
# May 21, 2021

shape = input("Which shape do you want to find the area of? ")

if shape == "rectangle":
    length = input("What's the length? ")
    width = input("What's the width? ")
    
    length = float(length)
    width = float(width)
    
    area = length * width
    print("The area is", area)

elif shape == "circle":
    radius = input("What's the radius? ")
    
    radius = float(radius)
    area = 3.14 * radius ** 2
    
    print("The area is", area)