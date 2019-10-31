import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with the given turtle, with
       each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(360/4)

def draw_square_from_center(some_turtle, side_length):
    '''Draws a square, starting and ending in the center of
       the square.'''
    # move to center
    some_turtle.penup()
    for counter in range(2):
        some_turtle.right(90)
        some_turtle.forward(side_length/2)
    some_turtle.pendown()
    some_turtle.left(180)
    
    draw_square(some_turtle, side_length)
    
    # move back to center
    some_turtle.penup()
    for counter in range(2):
        some_turtle.forward(side_length/2)
        some_turtle.left(90)
    some_turtle.pendown()
    some_turtle.left(180)

# setting up window and turtles
canvas = turtle.Screen()
iftemum = turtle.Turtle()
iftemum.shape("turtle")
iftemum.pensize(5)

#drawing 1
# draw_square_from_center(iftemum, 300)
# draw_square_from_center(iftemum, 200)

# drawing 2
# draw_square_from_center(iftemum, 200)
# iftemum.left(45)
# draw_square_from_center(iftemum, 200)

# drawing 3
draw_square_from_center(iftemum, 200)
draw_square(iftemum, 200)