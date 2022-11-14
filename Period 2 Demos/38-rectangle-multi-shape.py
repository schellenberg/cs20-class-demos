import turtle

def draw_rectangle(some_turtle, width, height):
    '''some_turtle -> turtle.Turtle() object
       width -> integer
       height -> integer
       
       Draws a rectangle with the given sizes,
       ending at the start, facing the same way it began.'''
    for side in [width, height, width, height]:
        some_turtle.forward(side)
        some_turtle.left(90)

window = turtle.Screen()
muhammad = turtle.Turtle()
muhammad.pensize(5)

for rectangle in range(4):
    draw_rectangle(muhammad, 200, 75)
    muhammad.left(90)
