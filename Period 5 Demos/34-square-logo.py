import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side length
       is side_length long. Ends at the same spot it started.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_centre(a_turtle, side):
    '''Draws a square with a_turtle, where each side is side long.
       Starts and ends in the centre of the square.'''
    a_turtle.penup()
    a_turtle.backward(side/2)
    a_turtle.right(90)
    a_turtle.forward(side/2)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, side)
    a_turtle.penup()
    a_turtle.forward(side/2)
    a_turtle.left(90)
    a_turtle.forward(side/2)
    a_turtle.right(90)
    a_turtle.pendown()

canvas = turtle.Screen()
hao = turtle.Turtle()
hao.pensize(3)

#square logo
# draw_square_from_centre(hao, 150)
# hao.left(45)
# draw_square_from_centre(hao, 150)

#overlapped squares
# draw_square(hao, 150)
# draw_square_from_centre(hao, 150)

#inner squares
draw_square_from_centre(hao, 150)
draw_square_from_centre(hao, 200)