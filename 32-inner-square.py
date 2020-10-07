import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square from the bottom left with some_turtle, with each side being side_length long'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

def draw_square_from_center(a_turtle, side_length):
    '''Draws a square from the center point of the square'''
    #move to starting location
    a_turtle.penup()
    for counter in range(2):
        a_turtle.right(90)
        a_turtle.forward(side_length/2)
    a_turtle.right(180)
    a_turtle.pendown()
    
    #draw the square
    draw_square(a_turtle, side_length)
    
    #move to center again
    a_turtle.penup()
    a_turtle.forward(side_length/2)
    a_turtle.left(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(90)
    a_turtle.pendown()

canvas = turtle.Screen()
aman = turtle.Turtle()

draw_square_from_center(aman, 300)
draw_square_from_center(aman, 200)
