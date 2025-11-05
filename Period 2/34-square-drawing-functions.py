import turtle

def draw_square(the_turtle, side_length):
    '''Draw a square with the_turtle, where each side
       is side_length long'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

def draw_square_from_centre(some_turtle, side_length):
    '''Draws a square, starting and ending in the center of the
       square using some_turtle. Each side is side_length long.'''
    #heading to bottom left
    some_turtle.penup()
    some_turtle.backward(side_length/2)
    some_turtle.right(90)
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.pendown()

    draw_square(some_turtle, side_length)
    
    #head back to centre
    some_turtle.penup()
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
    some_turtle.right(90)
    some_turtle.pendown()
    
def draw_inner_squares(the_turtle, small_square, large_square):
    '''Draws two squares, one inside the other.'''
    draw_square_from_centre(the_turtle, small_square)
    draw_square_from_centre(the_turtle, large_square)

def draw_square_logo(my_turtle, the_side_length):
    '''Draws two squares, one rotated by 45 degrees.'''
    draw_square_from_centre(my_turtle, the_side_length)
    my_turtle.left(45)
    draw_square_from_centre(my_turtle, the_side_length)

canvas = turtle.Screen()
artin = turtle.Turtle()
artin.pensize(5)
artin.speed(0)

# draw_inner_squares(artin, 150, 200)
draw_square_logo(artin, 300)

