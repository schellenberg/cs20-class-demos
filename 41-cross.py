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

def draw_inner_squares(my_turtle, inner_side_length, outer_side_length):
    draw_square(my_turtle, inner_side_length)
    buffer = (outer_side_length - inner_side_length) / 2
    
    # go to start of bigger square
    my_turtle.penup()
    for move in range(2):
        my_turtle.right(90)
        my_turtle.forward(buffer)
    my_turtle.pendown()
    my_turtle.left(180)
    
    draw_square(my_turtle, outer_side_length)


window = turtle.Screen()
rylan = turtle.Turtle()
rylan.pensize(4)
rylan.speed(0)

quinten = turtle.Turtle()
quinten.pensize(10)
quinten.color("red")

#draw_cross(rylan, 150)
#draw_cross(quinten, 200)
#draw_square(rylan, 200)
draw_inner_squares(rylan, 200, 300)
