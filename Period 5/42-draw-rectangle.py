import turtle

def draw_rectangle(some_turtle, short_side_length, long_side_length):
    '''Draws a rectangle using some_turtle, drawing the long_side first
       then the short_side.'''
    for counter in range(2):
        some_turtle.forward(long_side_length)
        some_turtle.left(90)
        some_turtle.forward(short_side_length)
        some_turtle.left(90)
        
window = turtle.Screen()
emmett = turtle.Turtle()
emmett.pensize(5)

for rectangle in range(4):
    draw_rectangle(emmett, 75, 250)
    emmett.left(90)
