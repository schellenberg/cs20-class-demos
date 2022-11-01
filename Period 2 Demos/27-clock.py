import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

affan = turtle.Turtle()
affan.shape("turtle")
affan.color("blue")
affan.pensize(4)

#draw the clock
for hour in range(12):
    #draw one tick mark
    affan.penup()
    affan.forward(150)
    affan.pendown()
    affan.forward(25)
    affan.penup()
    affan.forward(25)
    affan.stamp()
    affan.backward(200)
    
    affan.left(360/12)
