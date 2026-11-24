import turtle

def draw_rectangle(some_turtle, short_side, long_side):
    '''Draws a rectangle with some_turtle, using short_side and long_side as lengths.'''
    for side in [long_side, short_side, long_side, short_side]:
        some_turtle.forward(side)
        some_turtle.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

robin = turtle.Turtle()
robin.pensize(3)

for shape in range(8):
    draw_rectangle(robin, 50, 200)
    robin.left(90)
    robin.forward(50)
    robin.right(90)
    robin.left(360/8)
