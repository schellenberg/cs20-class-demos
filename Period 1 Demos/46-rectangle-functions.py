import turtle

def draw_rectangle(a_turtle, length, width):
    '''Draws a rectangle with a_turtle, starting with the
       side being length long, then width long.'''
    for side_length in [length, width, length, width]:
        a_turtle.forward(side_length)
        a_turtle.left(90)

window = turtle.Screen()
radia = turtle.Turtle()
radia.pensize(4)
radia.speed(0)

for rectangle in range(8):
    draw_rectangle(radia, 125, 50)
    radia.left(90)
    radia.forward(50)
    radia.right(90)
    radia.left(360/8)
