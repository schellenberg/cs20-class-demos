import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

judah = turtle.Turtle()
judah.color("darkblue")
judah.pensize(5)

judah.left(45)
for side in range(4):
    judah.forward(200)
    judah.left(90)