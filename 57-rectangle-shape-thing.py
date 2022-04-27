import turtle

def draw_rectangle(some_turtle, width, height):
    '''Draws a rectangle, starting and ending in the bottom left corner.'''
    for sides in range(2):
        some_turtle.forward(width)
        some_turtle.left(90)
        some_turtle.forward(height)
        some_turtle.left(90)

def draw_rectangle_polygon(a_turtle, width, height, sides):
    '''Uses 'sides' rectangles, to draw a regular polygon.'''
    for rectangle in range(sides):
        draw_rectangle(a_turtle, width, height)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.right(90)
        a_turtle.left(360/sides)

canvas = turtle.Screen()

hermann = turtle.Turtle()
hermann.color("red")
hermann.pensize(3)

draw_rectangle_polygon(hermann, 200, 50, 8)
