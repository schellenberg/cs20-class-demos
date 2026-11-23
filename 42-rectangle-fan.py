import turtle

def draw_rectangle(some_turtle, short_side, long_side):
    '''Draws a rectangle with some_turtle, using short_side and long_side as lengths.'''
    for side in [long_side, short_side, long_side, short_side]:
        some_turtle.forward(side)
        some_turtle.left(90)

def draw_rectangle_fan(a_turtle, length, width):
    '''Draws four rectangle to make a fan type shape.'''
    for rectangle in range(4):
        draw_rectangle(a_turtle, width, length)
        bruno.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

bruno = turtle.Turtle()
bruno.pensize(3)

draw_rectangle_fan(bruno, 100, 25)