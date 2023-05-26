import turtle

window = turtle.Screen()
ayman = turtle.Turtle()

instructions = "FF-FF++FF-FF"

for task in instructions:
    if task == "F":
        ayman.forward(25)
    elif task == "+":
        ayman.right(45)
    elif task == "-":
        ayman.left(45)