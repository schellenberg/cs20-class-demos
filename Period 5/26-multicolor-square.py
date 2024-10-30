import turtle

the_screen = turtle.Screen()
ceberta = turtle.Turtle()
ceberta.pensize(10)

for line_color in ["green", "yellow", "blue", "red"]:
    ceberta.color(line_color)
    ceberta.forward(100)
    ceberta.left(90)
    
