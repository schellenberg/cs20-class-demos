import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

angelina = turtle.Turtle()
angelina.shape("turtle")
angelina.color("blue")
angelina.pensize(10)

#draw a triangle
for the_side in range(3):
    angelina.forward(200)
    angelina.left(360/3)
    
canvas.exitonclick()