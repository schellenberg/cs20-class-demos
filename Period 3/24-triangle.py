import turtle

canvas = turtle.Screen()
canvas.bgcolor("darkblue")

hazel = turtle.Turtle()
hazel.color("pink")
hazel.pensize(5)
hazel.shape("turtle")

#make hazel draw a triangle
for side in range(3):
    hazel.forward(200)
    hazel.left(360/3)