import turtle

#set up window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#create rafsan
rafsan = turtle.Turtle()
rafsan.shape("turtle")
rafsan.color("green")
rafsan.pensize(10)

#create natasha
natasha = turtle.Turtle()
natasha.shape("turtle")
natasha.color("red")
natasha.pensize(3)

# draw a square with natasha
for side in range(4):
    natasha.right(90)
    natasha.forward(100)

# draw a pentagon (5-sided shape) with rafsan
for side in range(5):
    rafsan.forward(100)
    rafsan.left(360/5)

canvas.exitonclick()
