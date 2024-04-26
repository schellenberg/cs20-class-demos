#square logo

import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.
       Starts and ends at the bottom left corner.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
def draw_square_from_centre(my_turtle, side_length):
    '''Draws a square with my_turtle, with each side side_length long.
       Starts and ends in the centre of the square.'''
    
    #moving to bottom left corner
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.left(180)
    my_turtle.pendown()

    draw_square(my_turtle, side_length)
    
    #move back to the centre
    my_turtle.penup()
    my_turtle.left(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.pendown()

canvas = turtle.Screen()
dinel = turtle.Turtle()
dinel.pensize(5)

draw_square_from_centre(dinel, 200)
dinel.left(45)
draw_square_from_centre(dinel, 200)
