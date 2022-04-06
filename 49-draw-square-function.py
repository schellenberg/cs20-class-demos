import turtle

def draw_square(some_turtle, side_length, the_color, pen_thickness):
    """Draws a square with the given some_turtle object, with each
       side being side_length long. Sets the color and pensize as well."""
    some_turtle.color(the_color)
    some_turtle.pensize(pen_thickness)
    
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
    
window = turtle.Screen()
victor = turtle.Turtle()

draw_square(victor, 200, "red", 6)
draw_square(victor, 50, "black", 2)