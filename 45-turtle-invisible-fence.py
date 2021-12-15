import turtle
import random

def is_within_fence(some_turtle):
    if some_turtle.xcor() > 150 or some_turtle.xcor() < -150:
        return False
    elif some_turtle.ycor() > 150 or some_turtle.ycor() < -150:
        return False
    else:
        return True

# setup window and turtle
window = turtle.Screen()
alex = turtle.Turtle()
alex.color("green")
alex.shape("turtle")

# pick random direction to move
angle = random.randrange(0, 360)
alex.left(angle)

#keep moving forward
while is_within_fence(alex):
    alex.forward(2)
    