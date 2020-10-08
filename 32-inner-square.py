import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square from the bottom left with some_turtle, with each side being side_length long'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_center(a_turtle, side_length):
    '''Draws a square from the center point of the square'''
    #move to starting location
    a_turtle.penup()
    for counter in range(2):
        a_turtle.right(90)
        a_turtle.forward(side_length/2)
    a_turtle.right(180)
    a_turtle.pendown()
    
    #draw the square
    draw_square(a_turtle, side_length)
    
    #move to center again
    a_turtle.penup()
    a_turtle.forward(side_length/2)
    a_turtle.left(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(90)
    a_turtle.pendown()

def draw_inner_squares(my_turtle, outside_length, inside_length):
    '''Draws two squares, with the larger and smallers sizes given'''
    draw_square_from_center(my_turtle, outside_length)
    draw_square_from_center(my_turtle, inside_length)

def draw_square_logo(some_turtle, square_size):
    '''Draws two squares, one that is tilted by 45 degrees'''
    draw_square_from_center(some_turtle, square_size)
    some_turtle.left(45)
    draw_square_from_center(some_turtle, square_size)
    some_turtle.right(45)

def draw_overlapped_squares(my_turtle, size):
    '''Draws two squares, with one halfway over the other.'''
    draw_square_from_center(my_turtle, size)
    draw_square(my_turtle, size)

canvas = turtle.Screen()
aman = turtle.Turtle()

draw_overlapped_squares(aman, 300)