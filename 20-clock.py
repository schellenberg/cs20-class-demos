import turtle

#setup window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup turtle
hayden = turtle.Turtle()
hayden.shape("turtle")
hayden.color("blue")
hayden.pensize(4)

for hour in range(12):
    #draw one line
    hayden.penup()
    hayden.forward(100)
    hayden.pendown()
    hayden.forward(25)
    hayden.penup()
    hayden.forward(25)
    hayden.stamp()
    hayden.backward(150)
    
    hayden.left(360/12)
