import turtle

def draw_multicolor_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side
       is side_length long, and are different colors.'''
    for side_color in ['red', 'blue', 'yellow', 'purple']:
        some_turtle.color(side_color)
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
        
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

audrey = turtle.Turtle()
audrey.pensize(3)

the_size = 20
for square in range(15):
    draw_multicolor_square(audrey, the_size)
    the_size = the_size + 10
    audrey.forward(10)
    audrey.right(18)


