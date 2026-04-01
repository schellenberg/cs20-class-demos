import turtle

canvas = turtle.Screen()

matthew = turtle.Turtle()
matthew.color("red")
matthew.pensize(5)

quan = turtle.Turtle()
quan.color("maroon")
quan.pensize(10)
quan.penup()
quan.backward(300)
quan.pendown()

#draw a pentagon (5 sided shape) with Matthew
for side in range(5):
    matthew.forward(200)
    matthew.left(360/5)

#draw a triangle with quan
for the_color in ["red", "blue", "yellow"]:
    quan.color(the_color)
    quan.forward(150)
    quan.left(360/3)
    
