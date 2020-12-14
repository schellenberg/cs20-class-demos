import turtle

canvas = turtle.Screen()
kyran = turtle.Turtle()
kyran.speed(0)

instructions = "F+F+F+F"

for task in instructions:
    if task == "F":
        kyran.forward(50)
    elif task == "+":
        kyran.right(45)
    elif task == "-":
        kyran.left(45)