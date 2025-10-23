import turtle

the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

ali = turtle.Turtle()
ali.pensize(20)

for the_color in ["yellow", "red", "blue", "purple"]:
    ali.color(the_color)
    ali.forward(200)
    ali.left(90)