import turtle

def draw_rectangle(a_turtle, short_side, long_side):
    for side in [long_side, short_side, long_side, short_side]:
        a_turtle.forward(side)
        a_turtle.left(90)
        
canvas = turtle.Screen()
jace = turtle.Turtle()
jace.pensize(5)
jace.speed(0)

for rectangle in range(8):
    draw_rectangle(jace, 50, 200)
    jace.left(90)
    jace.forward(50)
    jace.right(90)
    jace.left(360/8)
