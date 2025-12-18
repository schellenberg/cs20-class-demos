import turtle

def draw_instructions(instructions, some_turtle, length, angle):
    '''Draws with some_turtle, going one by one in the instructions.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(length)
        elif task == "-":
            some_turtle.left(angle)
        elif task == "+":
            some_turtle.right(angle)

canvas = turtle.Screen()
mitt = turtle.Turtle()

instructions = "F++FF++F++FF"
draw_instructions(instructions, mitt, 100, 45)