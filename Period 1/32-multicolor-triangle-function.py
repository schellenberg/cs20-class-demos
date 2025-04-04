import turtle

def draw_triangle(a_turtle, side_length):
    '''Draws a triangle with a_turtle, with each side side_length long.'''
    for the_color in ["red", "blue", "green"]:
        a_turtle.color(the_color)
        a_turtle.forward(side_length)
        a_turtle.left(360/3)

canvas = turtle.Screen()
canvas.bgcolor("lightblue")

lacon = turtle.Turtle()
lacon.color("red")
lacon.pensize(5)

draw_triangle(lacon, 300)