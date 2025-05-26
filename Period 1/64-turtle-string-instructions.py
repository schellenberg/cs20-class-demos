import turtle

def draw_instructions(some_turtle, instructions, length, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(length)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
joel = turtle.Turtle()
joel.shape("turtle")

shape = "FF++F++FF++F"
draw_instructions(joel, shape, 50, 45)
