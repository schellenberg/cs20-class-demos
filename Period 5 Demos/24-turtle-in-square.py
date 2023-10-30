import turtle
import random

canvas = turtle.Screen()

bob = turtle.Turtle()

# draw a square to represent the area the turtle needs to stay inside
bob.speed(0)
bob.penup()
bob.goto(-100, -100) # sends bob to a specific coordinate
bob.pendown()
for side in range(4):
    bob.forward(200)
    bob.left(90)
bob.penup()

# reset turtle to normal starting location
bob.goto(0, 0)
bob.speed(3)

# pick random direction to move
some_angle = random.randrange(1, 360)
bob.setheading(some_angle)

#     right wall            left wall              top wall              bottom wall              
while bob.xcor() <= 100 and bob.xcor() >= -100 and bob.ycor() <= 100 and bob.ycor() >= -100:
    bob.forward(5)


