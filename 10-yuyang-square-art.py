import turtle

def draw_row(some_turtle, the_colors, size):
    for this_color in the_colors:
        some_turtle.fillcolor(this_color)
        some_turtle.begin_fill()
        for counter in range(4):
            some_turtle.forward(size)
            some_turtle.left(90)
        some_turtle.end_fill()
        some_turtle.forward(size)

canvas = turtle.Screen()
yuyang = turtle.Turtle()

row = ["black", "black", "blue", "red", "yellow", "black", "black"]
draw_row(yuyang, row, 20)
