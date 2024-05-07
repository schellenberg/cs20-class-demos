import turtle
import random

STEP_SIZE = 50

def is_on_screen(window, the_turtle):
    '''Returns True if the_turtle is inside the bounds of
       the given window.'''
    right_side = window.window_width() / 2
    left_side = -window.window_width() / 2
    top_side = window.window_height() / 2
    bottom_side = -window.window_height() / 2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    return x > left_side and x < right_side and y < top_side and y > bottom_side

canvas = turtle.Screen()
albert = turtle.Turtle()
albert.shape("turtle")
albert.pensize(3)

while is_on_screen(canvas, albert):
    albert.forward(STEP_SIZE)
    
    choice = random.randrange(3)
    if choice == 0:
        albert.left(90)
    elif choice == 1:
        albert.right(90)
    #if it's a 2, just leave it. It's going straight...
    
        
print("It's over. I'm off the screen.")

