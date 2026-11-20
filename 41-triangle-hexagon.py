import turtle

def draw_triangle(a_turtle, side_length):
    '''Draws a triangle with a_turtle, where each side is side_length long.'''
    for side in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(360/3)

def draw_triangle_hexagon(some_turtle, length):
    '''Draws a hexagon using 6 triangles, with each side length long.'''
    for triangle in range(6):
        draw_triangle(some_turtle, length)
        some_turtle.left(60)

window = turtle.Screen()
window.bgcolor("lightgreen")

himal = turtle.Turtle()
himal.color("blue")
himal.pensize(4)

draw_triangle_hexagon(himal, 200)

