import turtle

def draw_instructions(some_turtle, instructions, distance, angle):
    '''Draw each instruction with some_turtle, moving forward by
       distance, and turning by angle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
charlie = turtle.Turtle()

instructions = "FF++FFF++FF++FFF"
draw_instructions(charlie, instructions, 100, 45)

        
