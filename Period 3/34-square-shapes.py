import turtle

def draw_square(a_turtle, side_length):
    '''Draws a square with a_turtle, where each side
       is side_length long.'''
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)

def draw_square_from_center(some_turtle, side_length):
    '''Draws a sqaure with some_turtle, and starts and ends in
       the center of the square.'''
    #go to bottom left
    some_turtle.penup()
    some_turtle.backward(side_length/2)
    some_turtle.right(90)
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.pendown()
    
    draw_square(some_turtle, side_length)
    
    #go back to center
    some_turtle.penup()
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
    some_turtle.right(90)
    some_turtle.pendown()

canvas = turtle.Screen()
kai = turtle.Turtle()
kai.pensize(3)
kai.speed(0)

#inner squares
# draw_square_from_center(kai, 150)
# draw_square_from_center(kai, 200)

#square logo
# draw_square_from_center(kai, 200)
# kai.left(45)
# draw_square_from_center(kai, 200)

#overlapping squares
draw_square_from_center(kai, 200)
draw_square(kai, 200)





