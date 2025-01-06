import turtle

window = turtle.Screen()
khoi = turtle.Turtle()

tasks = "FF++F++FF++F"
for task in tasks:
    if task == "F":
        khoi.forward(25)
    elif task == "+":
        khoi.right(45)
    elif task == "-":
        khoi.left(45)
        