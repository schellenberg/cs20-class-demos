import turtle
import random

def is_in_screen(the_window, the_turtle):
    '''Returns True if the_turtle is within the_window.'''
    left = -(the_window.window_width() / 2)
    right = the_window.window_width() / 2
    top = the_window.window_height() / 2
    bottom = -(the_window.window_height() / 2)
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    if x > left and x < right and y < top and y > bottom:
        return True
    else:
        return False

STEP_SIZE = 50

canvas = turtle.Screen()

nathan = turtle.Turtle()
nathan.shape("turtle")
nathan.pensize(3)

options = ["left", "right", "straight"]

while is_in_screen(canvas, nathan):
    direction = random.choice(options)
    if direction == "left":
        nathan.left(90)
    elif direction == "right":
        nathan.right(90)
    # if going straight, ignore it, since we're not turning
    nathan.forward(STEP_SIZE)
    
print("I'm off the screen!")    
    