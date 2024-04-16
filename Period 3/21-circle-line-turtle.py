import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

keiran = turtle.Turtle()
keiran.shape("turtle")
keiran.pensize(8)
keiran.speed(0)

#draw a circle
keiran.left(90)
for side in range(360):
    keiran.forward(1)
    keiran.right(1)
    
keiran.right(90)
keiran.backward(25)
keiran.forward(160)
keiran.hideturtle()
