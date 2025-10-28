import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

isabella = turtle.Turtle()
isabella.shape("turtle")
isabella.penup()
isabella.speed(0)

for step in range(10, 200, 2):
    isabella.forward(step)
    isabella.left(50)
    isabella.stamp()