import turtle

screen = turtle.Screen()

victor = turtle.Turtle()
victor.pensize(3)
victor.shape("turtle")

for side in [100,25,125,150,125,25,100]:
    victor.forward(side)
    victor.right(90)

victor.right(180)
victor.forward(100)