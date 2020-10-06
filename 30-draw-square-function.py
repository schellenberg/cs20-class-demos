import turtle

def draw_square(some_turtle, side_length):
    '''Make some_turtle draw a square, with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
    

canvas = turtle.Screen()
kieran = turtle.Turtle()
aidan = turtle.Turtle()
aidan.color("red")
aidan.pensize(4)

draw_square(kieran, 100)
draw_square(aidan, 300)