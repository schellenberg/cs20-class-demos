import turtle

def draw_square(my_turtle, side_length):
    '''Draws a square with each side being side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)
        
def draw_square_from_center(my_turtle, side_length):
    '''Draws a sqaure, starting and ending in the center of the square.'''
    my_turtle.penup()
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(180)
    my_turtle.pendown()
    draw_square(my_turtle, side_length)
    my_turtle.penup()
    my_turtle.forward(side_length/2)
    my_turtle.left(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)

def draw_inner_squares(a_turtle, inner_side, outer_side):
    '''Draws an outer and inner square, based on the sizes you pass in.'''
    buffer = (outer_side - inner_side) * 0.5
    draw_square(a_turtle, inner_side)
    a_turtle.penup()
    a_turtle.backward(buffer)
    a_turtle.right(90)
    a_turtle.forward(buffer)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, outer_side)


#setup window and turtle
window = turtle.Screen()
umar = turtle.Turtle()

draw_square_from_center(umar, 250)
umar.left(45)
draw_square_from_center(umar, 250)