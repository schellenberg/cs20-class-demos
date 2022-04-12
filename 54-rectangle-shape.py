import turtle

def draw_rectangle(a_turtle, width, height):
    for the_l in range(2):
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)

window = turtle.Screen()
ivy = turtle.Turtle()
ivy.pensize(5)

for shape in range(4):
    draw_rectangle(ivy, 200, 75)
    ivy.left(90)
