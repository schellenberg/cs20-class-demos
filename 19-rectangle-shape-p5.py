import turtle

window = turtle.Screen()

ray = turtle.Turtle()
ray.pensize(4)

def draw_rectangle(some_turtle, side_length, side_width):
    for distance in range(2):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        some_turtle.forward(side_width)
        some_turtle.left(90)
    some_turtle.left(90)
    some_turtle.forward(side_width)
    some_turtle.right(90)

for rectangle in range(8):
    draw_rectangle(ray, 300, 75)
    ray.left(360/8)