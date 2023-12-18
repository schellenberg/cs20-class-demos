import turtle

canvas = turtle.Screen()
justin = turtle.Turtle()

instructions = "FF++F++FF++F"

for task in instructions:
    if task == "F":
        justin.forward(50)
    elif task == "+":
        justin.right(45)
    elif task == "-":
        justin.left(45)