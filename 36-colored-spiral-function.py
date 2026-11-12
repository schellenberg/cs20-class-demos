import turtle

def draw_square(some_turtle, side_length, the_color):
    '''Draws a square with some_turtle, where each side is side_length long,
       and the lines are the_color.'''
    some_turtle.color(the_color)
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

#setup window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

nikita = turtle.Turtle()
nikita.shape("turtle")
nikita.pensize(4)
nikita.speed(0)

size = 20
for some_color in ["red", "purple", "blue", "green", "yellow", "black", "orange", "silver", "pink", "gold", "beige", "aquamarine", "crimson", "olive", "white", "magenta"]:
    draw_square(nikita, size, some_color)
    size += 10
    nikita.forward(10)
    nikita.right(20)
    