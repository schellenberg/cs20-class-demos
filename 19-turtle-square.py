import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

victor = turtle.Turtle()
victor.shape("turtle")
victor.color("purple")
victor.pensize(5)

victor.forward(175)
victor.left(90)
victor.forward(175)
victor.left(90)
victor.forward(175)
victor.left(90)
victor.forward(175)
victor.left(90)

canvas.exitonclick()  #close window when you click it
