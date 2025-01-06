import turtle

def draw_instructions(some_turtle, instructions, distance, angle):
    '''Draws the instructions using some_turtle, where each move
       is distance long, and the turns use angle.'''
    for letter in instructions:
        if letter == "F":
            some_turtle.forward(distance)
        elif letter == "+":
            some_turtle.right(angle)
        elif letter == "-":
            some_turtle.left(angle)
    
canvas = turtle.Screen()
aidan = turtle.Turtle()

instructions = "FF++F++FF++F"
draw_instructions(aidan, instructions, 50, 45)

        