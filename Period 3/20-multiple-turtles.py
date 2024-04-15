import turtle

# setup the screen
the_window = turtle.Screen()
the_window.bgcolor("black")

#setup a turtle
sumaiya = turtle.Turtle()
sumaiya.color("yellow")
sumaiya.shape("turtle")
sumaiya.pensize(7)

#setup another turtle
laeron = turtle.Turtle()
laeron.color("lightgreen")
laeron.pensize(14)
laeron.shape("turtle")

#setup one more turtle
chisom = turtle.Turtle()
chisom.color("white")
chisom.pensize(10)
chisom.shape("turtle")

#draw a pentagon
for side in range(5):
    sumaiya.forward(100)
    sumaiya.left(360/5)

#move to where I want to draw a triangle
laeron.penup()
laeron.backward(300)
laeron.pendown()

#draw a triangle
for side in range(3):
    laeron.forward(150)
    laeron.left(360/3)


#move to where I want to draw a square
chisom.penup()
chisom.backward(150)
chisom.right(90)
chisom.forward(250)
chisom.left(90)
chisom.pendown()

#draw a square
for the_color in ["blue", "green", "white", "yellow"]:
    chisom.color(the_color)
    chisom.forward(100)
    chisom.left(360/4)
    
    
    