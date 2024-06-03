import turtle

def draw_string(some_turtle, instructions, distance, angle):
    '''Use some_turtle to draw each step in the instructions,
       moving by distance, and turning by angle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

screen = turtle.Screen()
michael = turtle.Turtle()

instructions = "FF--FF--FF--FF--"
draw_string(michael, instructions, 25, 45)        
        