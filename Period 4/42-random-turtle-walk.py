import turtle
import random

def is_in_screen(the_turtle, the_window):
    right = the_window.window_width() / 2
    left = -right
    top = the_window.window_height() / 2
    bottom = -top
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    if x > left and x < right and y < top and y > bottom:
        return True
    else:
        return False

STEP_SIZE = 50

canvas = turtle.Screen()
tyler = turtle.Turtle()
tyler.shape("turtle")
tyler.pensize(3)

options = ["left", "right", "straight"]
while is_in_screen(tyler, canvas):
    direction = random.choice(options)
    if direction == "right":
        tyler.right(90)
    elif direction == "left":
        tyler.left(90)
    # if going straight, just don't do anything
    tyler.forward(STEP_SIZE)
    
print("I'm off the screen!")    
    