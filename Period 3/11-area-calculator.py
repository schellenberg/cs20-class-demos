# Area Calculator
# Dan Schellenberg
# March 26, 2024

# ask which shape to calculate the area of
shape = input("Which shape do you want to calculate the are of? ")

# deal with rectangle
if shape == "rectangle":
    width = input("What's the width? ")
    height = input("What's the height? ")
    
    width = float(width)
    height = float(height)
    
    area = width * height
    
    print("The area of the rectangle is " + str(area))

# deal with circle
elif shape == "circle":
    radius = input("What's the radius? ")
    
    radius = float(radius)
    
    area = 3.14 * radius ** 2
    
    print("The area of the circle is " + str(area))

# deal with triangle
