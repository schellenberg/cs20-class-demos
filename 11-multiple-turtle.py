import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

darren = turtle.Turtle()
darren.shape("turtle")
darren.pensize(5)
darren.speed(0)

for square in range(15):
    #draw a square
    for some_color in ["purple", "yellow", "orange", "red"]:
        darren.color(some_color)
        darren.forward(100)
        darren.left(90)
    darren.left(360/15)

ari = turtle.Turtle()
ari.color("blue")
ari.pensize(5)

#draw a triangle
for side in range(3):
    ari.forward(100)
    ari.left(360/3)
