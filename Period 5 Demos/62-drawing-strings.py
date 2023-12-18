import turtle

def draw_instructions(some_turtle, instructions, angle, distance):
    '''Draw a shape based on the instructions given.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

window = turtle.Screen()
evan = turtle.Turtle()

instructions = "F++F++F"
draw_instructions(evan, instructions, 60, 50)
