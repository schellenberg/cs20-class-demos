import turtle

window = turtle.Screen()
arham = turtle.Turtle()
arham.speed(1)
arham.pensize(10)

for side_color in ["yellow", "green", "red", "black"]:
    arham.color(side_color)
    arham.forward(100)
    arham.left(90)