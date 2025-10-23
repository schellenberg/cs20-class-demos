import turtle

canvas = turtle.Screen()

yasin = turtle.Turtle()
yasin.shape("turtle")
yasin.pensize(20)

for the_color in ["red", "yellow", "blue", "green"]:
    yasin.color(the_color)
    yasin.forward(200)
    yasin.left(90)