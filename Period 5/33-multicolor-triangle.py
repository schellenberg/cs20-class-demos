import turtle

def draw_triangle(a_turtle, the_length):
    '''Draws a triangle with a_turtle.
       Every side is the_length long.'''
    for the_color in ["red", "blue", "green"]:
        a_turtle.color(the_color)
        a_turtle.forward(the_length)
        a_turtle.left(360/3)

window = turtle.Screen()
window.bgcolor("lightgreen")

sam = turtle.Turtle()
sam.pensize(5)

draw_triangle(sam, 200)