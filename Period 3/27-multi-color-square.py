import turtle

canvas = turtle.Screen()
tarush = turtle.Turtle()
tarush.pensize(7)

for line_color in ["yellow", "blue", "red", "green"]:
    tarush.color(line_color)
    tarush.forward(100)
    tarush.left(90)