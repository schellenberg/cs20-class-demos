import turtle

def draw_multicolor_square(a_turtle, side_length, color_list):
    '''Draws a square with a_turtle, where each side
       is side_length long. Each side will also be
       a different color.'''
    for the_color in color_list:
        a_turtle.color(the_color)
        a_turtle.forward(side_length)
        a_turtle.left(90)

#setup window
window = turtle.Screen()
window.bgcolor("lightgreen")

#setup turtle
ashad = turtle.Turtle()
ashad.pensize(4)
ashad.speed(0)

the_colors = ["red", "blue", "green", "yellow"]
the_size = 20
for square in range(20):
    draw_multicolor_square(ashad, the_size, the_colors)
    the_size = the_size + 10
    ashad.forward(10)
    ashad.right(15)

