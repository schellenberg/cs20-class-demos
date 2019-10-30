import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with the some_turtle passed in,
       with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

# set up window and turtle
window = turtle.Screen()

amy = turtle.Turtle()
amy.shape("turtle")
amy.pensize(4)

noah = turtle.Turtle()
noah.shape("turtle")
noah.pensize(7)
noah.color("green")

# draw some shapes
draw_square(amy, 200)
draw_square(noah, 100)