import turtle

#set up window
window = turtle.Screen()
window.bgcolor("black")

#set up turtles
dayton = turtle.Turtle()
dayton.color("red")
dayton.pensize(8)

azka = turtle.Turtle()
azka.color("blue")
azka.shape("turtle")
azka.pensize(15)

#draw a pentagon
for side in range(5):
    dayton.forward(200)
    dayton.left(360/5)
    
#draw a triangle
for side in range(3):
    azka.forward(200)
    azka.left(360/3)

