import turtle

#setup window
the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

#setup turtle
leo = turtle.Turtle()
leo.shape("turtle")
leo.color("blue")
leo.pensize(5)

nauman = turtle.Turtle()
nauman.shape("turtle")
nauman.color("white")
nauman.pensize(10)
nauman.penup()
nauman.backward(250)
nauman.pendown()

#draw a square with leo
for counter in range(4):
    leo.forward(100)
    leo.left(90)
    
#draw a triangle with nauman
for side in range(3):
    nauman.forward(150)
    nauman.left(120)
    