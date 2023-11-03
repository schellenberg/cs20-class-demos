import turtle

def draw_square(some_turtle, size):
    '''Use some_turtle to draw a square, with each side being size length long.'''
    for side in range(4):
        some_turtle.forward(size)
        some_turtle.left(90)

def draw_cross(some_turtle, side_length):
    '''Draw a cross shape with some_turtle, where each side is side_length long.'''
    for u_shape in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)
        
        
canvas = turtle.Screen()
winston = turtle.Turtle()
winston.color("red")

shreya = turtle.Turtle()
shreya.color("blue")
shreya.shape("turtle")

#draw_square(winston, 150)
#draw_square(shreya, 250)

draw_cross(winston, 100)
