import turtle

def draw_cross(some_turtle, side_length):
    for u_shape in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)

def draw_square(my_turtle, length_of_side):
    for side in range(4):
        my_turtle.forward(length_of_side)
        my_turtle.left(90)

def draw_inner_squares(a_turtle, small_side_length, large_side_length):
    draw_square(a_turtle, small_side_length)
    buffer = (large_side_length - small_side_length) / 2
    
    a_turtle.penup()
    for move in range(2):
        a_turtle.right(90)
        a_turtle.forward(buffer)
    a_turtle.left(180)
    a_turtle.pendown()
    
    draw_square(a_turtle, large_side_length)

screen = turtle.Screen()
screen.bgcolor("red")
cooper = turtle.Turtle()
cooper.pensize(4)

blake = turtle.Turtle()
blake.pensize(8)
blake.color("white")

draw_inner_squares(blake, 250, 300)
