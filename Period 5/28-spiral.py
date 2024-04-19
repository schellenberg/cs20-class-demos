import turtle

the_canvas = turtle.Screen()
the_canvas.bgcolor("lightgreen")

riley = turtle.Turtle()
riley.shape("turtle")
riley.color("red")
riley.penup()
riley.speed(0)

for step in range(10, 800, 1):
    riley.forward(step)
    riley.stamp()
    riley.left(95)
