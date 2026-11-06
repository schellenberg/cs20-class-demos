import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

yulin = turtle.Turtle()
yulin.color("red")
yulin.shape("turtle")
yulin.penup()
yulin.speed(0)

for side_length in range(10, 500, 3):
    yulin.forward(side_length)
    yulin.left(50)
    yulin.stamp()
    
