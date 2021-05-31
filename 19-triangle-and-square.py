import turtle

# create the window
window = turtle.Screen()
window.bgcolor("lightgreen")

# setup the turtles
declan = turtle.Turtle()
declan.shape("turtle")
declan.color("pink")
declan.pensize(5)

hannah = turtle.Turtle()
hannah.penup()
hannah.backward(250)
hannah.pendown()
hannah.color("orange")
hannah.pensize(10)

# draw a triangle
for side in range(3):
    declan.forward(100)
    declan.left(120)

# draw a square
for the_color in ["red", "blue", "orange", "black"]:
    hannah.color(the_color)
    hannah.forward(150)
    hannah.left(90)

