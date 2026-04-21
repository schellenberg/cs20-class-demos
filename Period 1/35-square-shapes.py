import turtle

def draw_square(my_turtle, side_length):
    '''Draws a square with my_turtle, where each side is
       side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)
        
def draw_square_from_centre(some_turtle, side_length):
    '''Draws a square with some_turtle, where the turtle starts and
       ends in the centre of the square.'''
    #move to starting spot
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

window = turtle.Screen()
zeca = turtle.Turtle()
zeca.pensize(3)

#inner squares
# draw_square_from_centre(zeca, 200)
# draw_square_from_centre(zeca, 150)

#square logo
# draw_square_from_centre(zeca, 150)
# zeca.left(45)
# draw_square_from_centre(zeca, 150)

#overlapped squares
draw_square(zeca, 150)
draw_square_from_centre(zeca, 150)

