import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

maysie = turtle.Turtle()
maysie.shape("turtle")
maysie.color("purple")
maysie.penup()
maysie.speed(0)

for step in range(0, 50, 2):
    maysie.stamp()
    maysie.forward(step)
    maysie.left(20)
    
