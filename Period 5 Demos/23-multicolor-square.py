import turtle

canvas = turtle.Screen()
coen = turtle.Turtle()
coen.shape("turtle")
coen.pensize(10)

for the_color in ["red", "blue", "green", "purple"]:
    coen.color(the_color)
    coen.forward(200)
    coen.left(90)