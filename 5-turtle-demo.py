import turtle

window = turtle.Screen()

noah = turtle.Turtle()
noah.shape("turtle")
noah.color("blue")

for counter in range(6):
    noah.forward(100)
    noah.left(360/6)
