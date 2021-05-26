import turtle

canvas = turtle.Screen()
canvas.bgcolor("yellow")

aaron = turtle.Turtle()
aaron.shape("turtle")
aaron.color("blue")

for side in range(5):
    aaron.forward(150)
    aaron.left(360/5)