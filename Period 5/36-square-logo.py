import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square using some_turtle, with each side
       being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
def draw_square_from_center(the_turtle, side_length):
    '''Draws a square, starting and ending in the center of the square.'''
    #go to bottom left corner
    the_turtle.penup()
    the_turtle.backward(side_length/2)
    the_turtle.right(90)
    the_turtle.forward(side_length/2)
    the_turtle.left(90)
    the_turtle.pendown()
    
    draw_square(the_turtle, side_length)
    
    #go back to the center
    the_turtle.penup()
    the_turtle.forward(side_length/2)
    the_turtle.left(90)
    the_turtle.forward(side_length/2)
    the_turtle.right(90)
    the_turtle.pendown()

def draw_square_logo(a_turtle, side_length):
    '''Draws two squares, with one rotated 45 degrees.'''
    draw_square_from_center(a_turtle, side_length)
    a_turtle.left(45)
    draw_square_from_center(a_turtle, side_length)

canvas = turtle.Screen()
aurora = turtle.Turtle()
aurora.pensize(5)

draw_square_logo(aurora, 200)