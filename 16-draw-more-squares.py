import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with the some_turtle passed in,
       with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_centre(some_turtle, side_length):
    '''Draws a square, starting and ending in the center
       of the square.'''
    # go to bottom left corner
    some_turtle.penup()
    for counter in range(2):
        some_turtle.right(90)
        some_turtle.forward(side_length/2)
    some_turtle.left(180)
    some_turtle.pendown()
    draw_square(some_turtle, side_length)
    
    #return to center
    some_turtle.penup()
    for counter in range(2):
        some_turtle.forward(side_length/2)
        some_turtle.left(90)
    some_turtle.left(180)

# set up window and turtle
window = turtle.Screen()

amy = turtle.Turtle()
amy.shape("turtle")
amy.pensize(4)

# draw some shapes
draw_square_from_centre(amy, 300)
amy.left(45)
draw_square_from_centre(amy, 300)
