import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square using some_turtle, with each side
       being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(the_turtle, big_side, the_gap):
    '''Draws two squares, one inside the other with the_turtle.
       The big square is going to be big_side long.
       The small square is calculated using the_gap.'''
    draw_square(the_turtle, big_side)
    
    #move to draw the smaller one
    the_turtle.penup()
    the_turtle.forward(the_gap)
    the_turtle.left(90)
    the_turtle.forward(the_gap)
    the_turtle.right(90)
    the_turtle.pendown()
    
    draw_square(the_turtle, big_side - 2 * the_gap)


canvas = turtle.Screen()
shiv = turtle.Turtle()

draw_inner_squares(shiv, 250, 50)