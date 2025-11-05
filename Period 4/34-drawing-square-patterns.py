import turtle

def draw_square(the_turtle, side_length):
    '''Draws a square with the_turtle, where each
       side is side_length long.'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

def draw_square_from_centre(a_turtle, the_side_length):
    '''Draws a square with a_turtle, where you start and end
       in the middle of the square facing east.'''
    #go to bottom left corner
    a_turtle.penup()
    a_turtle.backward(the_side_length/2)
    a_turtle.right(90)
    a_turtle.forward(the_side_length/2)
    a_turtle.left(90)
    a_turtle.pendown()
    
    draw_square(a_turtle, the_side_length)
    
    #move back to middle
    a_turtle.penup()
    a_turtle.forward(the_side_length/2)
    a_turtle.left(90)
    a_turtle.forward(the_side_length/2)
    a_turtle.right(90)
    a_turtle.pendown()

def draw_inner_squares(some_turtle, small_square, large_square):
    '''Draws two squares, one inside the other.'''
    draw_square_from_centre(some_turtle, small_square)
    draw_square_from_centre(some_turtle, large_square)

def draw_square_logo(my_turtle, square_size):
    '''Draws two squares, with one of them rotated by 45 degrees.'''
    draw_square_from_centre(my_turtle, square_size)
    my_turtle.left(45)
    draw_square_from_centre(my_turtle, square_size)

canvas = turtle.Screen()
decker = turtle.Turtle()
decker.pensize(5)

# draw_inner_squares(decker, 50, 150)
draw_square_logo(decker, 200)



