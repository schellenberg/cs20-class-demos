import turtle

def draw_square(the_turtle, side_length):
    '''Draws a square with the_turtle, where each side is
       side_length long. Starts and ends in the bottom left corner.'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)
        
def draw_square_from_middle_of_side(some_turtle, length):
    '''Draws a square with some_turtle, where each side is length long.
       Starts and ends in the middle of one of the sides.'''
    some_turtle.right(90)
    some_turtle.forward(length/2)
    some_turtle.left(90)
    draw_square(some_turtle, length)
    some_turtle.left(90)
    some_turtle.forward(length/2)
    some_turtle.right(90)
    
window = turtle.Screen()
asma = turtle.Turtle()
asma.pensize(5)

for square in range(5):
    draw_square_from_middle_of_side(asma, 250)
    asma.left(360/5)


