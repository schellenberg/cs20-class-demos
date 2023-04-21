import turtle

def draw_rectangle(a_turtle, short_side, long_side):
    for side in [long_side, short_side, long_side, short_side]:
        a_turtle.forward(side)
        a_turtle.left(90)
        
canvas = turtle.Screen()
gabe = turtle.Turtle()
gabe.pensize(5)

for shape in range(4):
    draw_rectangle(gabe, 50, 200)
    gabe.left(90)
