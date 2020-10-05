import turtle

window = turtle.Screen()
window.bgcolor("black")

vraj = turtle.Turtle()
vraj.color("pink")
vraj.shape("turtle")
vraj.penup()
vraj.speed(0)

for size in range(5, 400, 2):
    vraj.stamp()
    vraj.forward(size)
    vraj.right(50)