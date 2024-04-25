#inner squares

import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_inner_squares(my_turtle, large_square_size, buffer_size):
    #draw larger square
    draw_square(my_turtle, large_square_size)

    #move to place to draw smaller square
    oleh.penup()
    oleh.forward(buffer_size)
    oleh.left(90)
    oleh.forward(buffer_size)
    oleh.right(90)
    oleh.pendown()

    #draw the smaller square
    draw_square(oleh, large_square_size - 2*buffer_size)


window = turtle.Screen()
oleh = turtle.Turtle()
oleh.pensize(5)

draw_inner_squares(oleh, 200, 20)
