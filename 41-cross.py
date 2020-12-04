import turtle

def draw_cross(some_turtle, side_length):
    for u_shape in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)

def draw_square(a_turtle, side_length):
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)


window = turtle.Screen()
rylan = turtle.Turtle()
rylan.pensize(4)

quinten = turtle.Turtle()
quinten.pensize(10)
quinten.color("red")

#draw_cross(rylan, 150)
#draw_cross(quinten, 200)
draw_square(rylan, 200)
