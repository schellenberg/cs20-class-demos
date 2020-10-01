import turtle

canvas = turtle.Screen()
canvas.bgcolor("yellow")

zain = turtle.Turtle()
zain.shape("turtle")
zain.color("blue")
zain.pensize(4)
zain.speed(0)

#this is how to draw a square with a while loop...
# counter = 0
# while counter < 4:
#     zain.forward(150)
#     zain.left(90)
#     counter = counter + 1
    

#this is how to draw a square with a for loop...
for shape in range(30):
    for side in range(4):
        zain.forward(150)
        zain.left(90)
    zain.left(360/30)
    
# canvas.exitonclick()
    