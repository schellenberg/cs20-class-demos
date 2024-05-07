import turtle
import random

STEP_SIZE = 50

def is_on_screen(window, the_turtle):
    '''Returns True if turtle is within the bounds of
       the screen. False otherwise.'''
    right_side = window.window_width() / 2
    left_side = -window.window_width() / 2
    top_side = window.window_height() / 2
    bottom_side = -window.window_height() / 2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    return x > left_side and x < right_side and y < top_side and y > bottom_side

canvas = turtle.Screen()
rey = turtle.Turtle()
rey.shape("turtle")
rey.pensize(3)

while is_on_screen(canvas, rey):
    choice = random.randrange(1, 4)
    if choice == 1:
        rey.left(90)
    elif choice == 2:
        rey.right(90)
    #if it's a 3, don't turn at all
    
    rey.forward(STEP_SIZE)

print("I'm off the screen now....")


