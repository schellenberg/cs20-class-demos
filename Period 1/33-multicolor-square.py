import turtle

def draw_multicolor_square(some_turtle, side_length, some_colors):
    '''Draws a square, with each sides color coming from some_colors,
       and the sides are all side_length long.'''
    for the_color in some_colors:
        some_turtle.color(the_color)
        some_turtle.forward(side_length)
        some_turtle.left(90)

#setup window
window = turtle.Screen()
window.bgcolor("lightgreen")

#setup turtle
tyrone = turtle.Turtle()
tyrone.pensize(4)
tyrone.speed(0)

#draw lots of squares
square_colors = ["red", "blue", "yellow", "green"]
the_size = 20
for square in range(20):
    draw_multicolor_square(tyrone, the_size, square_colors)
    the_size = the_size + 10
    tyrone.forward(10)
    tyrone.right(15)





    