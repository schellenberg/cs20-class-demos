import turtle

def draw_rectangle(some_turtle, width, height):
    for l_shape in range(2):
        some_turtle.forward(width)
        some_turtle.left(90)
        some_turtle.forward(height)
        some_turtle.left(90)

def weird_shape(my_turtle, number_of_rectangles, width, height):
    for rectangle in range(number_of_rectangles):
        draw_rectangle(my_turtle, width, height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.right(90)
        my_turtle.left(360/number_of_rectangles)
    
canvas = turtle.Screen()
canvas.tracer(2)

anu = turtle.Turtle()
anu.pensize(4)
anu.speed(0)

weird_shape(anu, 100, 150, 10)