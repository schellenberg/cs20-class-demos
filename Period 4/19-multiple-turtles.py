import turtle

#set up the window
the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

#set up turtle
poulomi = turtle.Turtle()
poulomi.shape("turtle")
poulomi.color("red")
poulomi.pensize(5)

damien = turtle.Turtle()
damien.shape("turtle")
damien.color("purple")

#move to starting point
damien.penup()
damien.backward(200)
damien.pendown()

#draw a pentagon with poulomi
for side in range(5):
    poulomi.forward(200)
    poulomi.left(360/5)
    
#draw a square with damien
for side in range(4):
    damien.forward(100)
    damien.left(90)
    
    