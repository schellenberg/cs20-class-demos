import turtle

def draw_string(some_turtle, intructions, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
utsho = turtle.Turtle()
# utsho.speed(1)

instructions = "FF++FF++FF++FF"
draw_string(utsho, instructions, 100, 45)
