import turtle

def draw_rectangle(a_turtle, long_side, short_side):
    '''Draws a rectangle with a_turtle, where the long side
       is drawn first, then the short side.'''
    for side in [long_side, short_side, long_side, short_side]:
        a_turtle.forward(side)
        a_turtle.left(90)

screen = turtle.Screen()
justin = turtle.Turtle()
justin.pensize(3)

for rectangle in range(4):
    draw_rectangle(justin, 200, 50)
    justin.left(360/4)
