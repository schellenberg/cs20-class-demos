import turtle

def draw_instructions(instructions, some_turtle, distance, angle):
    '''Draw each of the instructions with some_turtle. Use distance
       to move forward, and turn by the given angle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
kabeer = turtle.Turtle()

instructions = "F++FF++F++FF++"
draw_instructions(instructions, kabeer, 50, 45)


