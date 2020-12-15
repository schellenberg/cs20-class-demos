import turtle
import easygui_qt as easy

my_clones = []

canvas = turtle.Screen()
canvas.bgcolor("black")

quinten = turtle.Turtle()
quinten.shape("turtle")
quinten.color("red")
quinten.pensize(5)
quinten.speed(1)
quinten.shape("square")
quinten.penup()

step = 10

my_clones.append(quinten)
kyran = quinten.clone()
kyran.backward(step)

my_clones.append(kyran)
print(my_clones)

for counter in range(20):
    for some_turtle in my_clones:
        some_turtle.forward(step)
        
