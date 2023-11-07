import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side length
       is side_length long. Ends at the same spot it started.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_centre(a_turtle, side_length):
    '''Draws a square with a_turtle, where each side is side_length
       long. Starts and ends in the centre of the square.'''
    a_turtle.penup()
    a_turtle.backward(side_length/2)
    a_turtle.right(90)
    a_turtle.forward(side_length/2)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, side_length)
    a_turtle.penup()
    a_turtle.forward(side_length/2)
    a_turtle.left(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(90)
    a_turtle.pendown()

canvas = turtle.Screen()
riahan = turtle.Turtle()
riahan.pensize(3)

#square logo
draw_square_from_centre(riahan, 150)
riahan.left(45)
draw_square_from_centre(riahan, 150)


#overerlapping squares
# draw_square(riahan, 150)
# draw_square_from_centre(riahan, 150)


#inner squares
# draw_square_from_centre(riahan, 100)
# draw_square_from_centre(riahan, 150)