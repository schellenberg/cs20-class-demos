import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
      
def draw_square_from_center(the_turtle, side_length):
    '''Draw a square, and start and end in the center point.'''
    #go to bottom left corner
    the_turtle.penup()
    the_turtle.backward(side_length/2)
    the_turtle.right(90)
    the_turtle.forward(side_length/2)
    the_turtle.left(90)
    the_turtle.pendown()
    
    draw_square(the_turtle, side_length)
    
    #head back to center
    the_turtle.penup()
    the_turtle.forward(side_length/2)
    the_turtle.left(90)
    the_turtle.forward(side_length/2)
    the_turtle.right(90)
    the_turtle.pendown()
    
      
def draw_square_logo(the_turtle, side_length):
    '''Draws two squares, with one rotated 45 degrees.'''
    draw_square_from_center(the_turtle, side_length)
    the_turtle.left(45)
    draw_square_from_center(the_turtle, side_length)
        
canvas = turtle.Screen()
harry = turtle.Turtle()
harry.pensize(5)

draw_square_logo(harry, 100)