import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

sadie = turtle.Turtle()
sadie.shape("turtle")
sadie.color("blue")
sadie.penup()
sadie.speed(0)

for step_size in range(10, 100, 2):
    sadie.stamp()
    sadie.forward(step_size)
    sadie.right(20)
    

