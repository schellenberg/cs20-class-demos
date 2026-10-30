import turtle

#setup window
window = turtle.Screen()
window.bgcolor("lightpink")

#setup turtle
niuosha = turtle.Turtle()
niuosha.shape("turtle")
niuosha.color("green")
niuosha.pensize(8)

#draw a square
for some_color in ["yellow", "red", "purple", "white"]:
    niuosha.color(some_color)
    niuosha.forward(200)
    niuosha.left(90)


