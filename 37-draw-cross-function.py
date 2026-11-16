import turtle

def draw_cross(some_turtle, side_length):
    '''Draws a cross shape with some_turtle, where each side is side_length long.'''
    for u_shape in range(4):
        for line in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)
    

canvas = turtle.Screen()

jaden = turtle.Turtle()
jaden.shape("turtle")
jaden.pensize(4)

draw_cross(jaden, 150)