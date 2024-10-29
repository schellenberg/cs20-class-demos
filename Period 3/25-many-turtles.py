import turtle

the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

steven = turtle.Turtle()
steven.shape("turtle")
steven.pensize(5)
steven.color("purple")

khoi = turtle.Turtle()
khoi.color("orange")
khoi.pensize(8)
khoi.shape("turtle")

#draw me a pentagon - 5 sided shape
for side in range(5):
    steven.forward(100)
    steven.left(360/5)


#khoi draws a square
khoi.penup()
khoi.backward(300)
khoi.pendown()

for side in range(4):
    khoi.forward(75)
    khoi.left(90)
    

the_window.exitonclick()
