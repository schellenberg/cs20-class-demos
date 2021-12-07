import turtle

def draw_c(a_turtle, longest_side_length, width_of_c):
    short = width_of_c
    long = longest_side_length
    mid = long - short
    
    for side in [mid, short, long, long, long, short, mid, 2*short-long]:
        a_turtle.forward(side)
        a_turtle.left(90)

canvas = turtle.Screen()
eric = turtle.Turtle()
eric.pensize(4)

draw_c(eric, 250, 25)


# eric.forward(200)
# eric.left(90)
# eric.forward(50)
# eric.left(90)
# eric.forward(250)
# eric.left(90)
# eric.forward(250)
# eric.left(90)
# eric.forward(250)
# eric.left(90)
# eric.forward(50)
# eric.left(90)
# eric.forward(200)
# eric.right(90)
# eric.forward(150)