import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

bianca = turtle.Turtle()
bianca.color("purple")
bianca.pensize(4)

merrick = turtle.Turtle()
merrick.color("blue")
merrick.pensize(10)

#move merrick to starting location
merrick.penup()
merrick.backward(200)
merrick.pendown()

#make bianca draw a square
for a_color in ["yellow", "red", "green", "blue"]:
    bianca.color(a_color)
    bianca.forward(100)
    bianca.left(90)

#make merrick draw a triangle
for side in range(3):
    merrick.left(120)
    merrick.forward(100)


