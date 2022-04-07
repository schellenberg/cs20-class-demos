import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with the given turtle, with each side being
       side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_center(a_turtle, side_length):
    '''Draws a square, but starts from the middle point of
       the square, and ends at the starting point.'''
    
    #go to bottom left of square
    a_turtle.penup()
    for i in range(2):
        a_turtle.right(90)
        a_turtle.forward(side_length/2)
    a_turtle.right(180)
    a_turtle.pendown()
    
    draw_square(a_turtle, side_length)
    
    #go back to center
    a_turtle.penup()
    for i in range(2):
        a_turtle.forward(side_length/2)
        a_turtle.left(90)
    a_turtle.right(180)
    a_turtle.pendown()
    

window = turtle.Screen()
shadi = turtle.Turtle()

# inner squares
#draw_square_from_center(shadi, 150)
#draw_square_from_center(shadi, 200)


# square logo
draw_square_from_center(shadi, 300)
shadi.left(45)
draw_square_from_center(shadi, 300)

