import turtle

canvas = turtle.Screen()

yakup = turtle.Turtle()
yakup.pensize(10)

# draw a pentagon (5 sided shape)
for the_color in ["yellow", "brown", "orange", "red", "blue"]:
    yakup.color(the_color)
    yakup.forward(200)
    yakup.left(360/5)
