import turtle
import random

canvas = turtle.Screen()
fatma = turtle.Turtle()

coordinates = []
movements = ["left", "right", "straight"]

while True:
    task = random.choice(movements)
    if task == "left":
        fatma.left(90)
    elif task == "right":
        fatma.right(90)
    fatma.forward(10)

    x = round(fatma.xcor())
    y = round(fatma.ycor())

    if [x, y] in coordinates:
        print("I've been here before!")
        break

    coordinates.append([x, y])