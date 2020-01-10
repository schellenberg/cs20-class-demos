import turtle
import random

canvas = turtle.Screen()
anna = turtle.Turtle()

coordinates = [[0,0]]
options = ["left", "right", "straight"]

while True:
    task = random.choice(options)
    
    if task == "left":
        anna.left(90)
    elif task == "right":
        anna.right(90)
    anna.forward(10)

    x = round(anna.xcor())
    y = round(anna.ycor())
    
    if [x, y] in coordinates:
        print("I've been here before.")
        break
    
    coordinates.append([x, y])
