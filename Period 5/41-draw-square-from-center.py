import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side
       is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_center(some_turtle, side_length):
    '''Draws a square, but start and end in the center of the square.'''
    some_turtle.penup()
    for counter in range(2):
        some_turtle.right(90)
        some_turtle.forward(side_length/2)
    some_turtle.right(180)
    some_turtle.pendown()
    draw_square(some_turtle, side_length)
    some_turtle.penup()
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
    some_turtle.right(90)
    
def draw_inner_squares(a_turtle, long_side_length, short_side_length):
    '''Draws two squares, one inside the other. The larger square uses
       long_side_length for each side, and the smaller uses
       short_side_length. The gap between them is calculated by the
       function.'''
    draw_square_from_center(a_turtle, long_side_length)
    draw_square_from_center(a_turtle, short_side_length)

def draw_rotated_squares(some_turtle, side_length):
    '''Draw two squares, with one rotated 45 degrees.'''
    draw_square_from_center(some_turtle, side_length)
    some_turtle.left(45)
    draw_square_from_center(some_turtle, side_length)

def draw_overlapped_squares(some_turtle, side_length):
    '''Drawing two square, where one is normal, and the other is starting
       from the center of the first.'''
    draw_square(some_turtle, side_length)
    draw_square_from_center(some_turtle, side_length)

window = turtle.Screen()
window.bgcolor("lightgreen")

arbe = turtle.Turtle()
arbe.pensize(3)

# draw_square_from_center(arbe, 200)
# draw_inner_squares(arbe, 300, 200)
# draw_rotated_squares(arbe, 250)
draw_overlapped_squares(arbe, 200)
