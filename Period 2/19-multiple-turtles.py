import turtle

#set up window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#set up turtle
mehtab = turtle.Turtle()
mehtab.shape("turtle")
mehtab.pensize(10)
mehtab.color("teal")

kavya = turtle.Turtle()
kavya.shape("turtle")
kavya.color("purple")

#move to starting spot
kavya.penup()
kavya.backward(200)
kavya.pendown()

#draw a pentagon
for side in range(5):
    mehtab.forward(200)
    mehtab.left(360/5)
    
#draw a square with kavya
for side in range(4):
    kavya.forward(150)
    kavya.left(90)
    