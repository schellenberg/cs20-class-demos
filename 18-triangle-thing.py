import turtle

def draw_triangle(the_turtle, side_length):
    for side in range(3):
        the_turtle.forward(side_length)
        the_turtle.left(120)
        
def draw_triangle_hexagon_thing(a_turtle, length):
    for triangle in range(6):
        draw_triangle(a_turtle, length)
        a_turtle.left(360/6)


the_window = turtle.Screen()

alvin = turtle.Turtle()
alvin.pensize(4)

draw_triangle_hexagon_thing(alvin, 100)