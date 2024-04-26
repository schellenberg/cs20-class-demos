import turtle

def draw_square(the_turtle, side_length):
    '''Draws a square with the_turtle, where each side is
       side_length long. Starts and ends in the bottom left corner.'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

def draw_square_from_centre(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length
       long. Starts and ends in the centre of the square.'''
    #move to bottom left
    some_turtle.penup()
    some_turtle.backward(side_length/2)
    some_turtle.right(90)
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.pendown()
    
    draw_square(some_turtle, side_length)
    
    #move back to centre
    some_turtle.penup()
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
    some_turtle.right(90)
    some_turtle.pendown()


canvas = turtle.Screen()
mouad = turtle.Turtle()
mouad.pensize(5)

#inner squares
# draw_square_from_centre(mouad, 250)
# draw_square_from_centre(mouad, 200)

#square logo
# draw_square_from_centre(mouad, 200)
# mouad.left(45)
# draw_square_from_centre(mouad, 200)


#overlapped squares
draw_square(mouad, 200)
draw_square_from_centre(mouad, 200)




