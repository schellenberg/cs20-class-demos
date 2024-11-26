import turtle
import random

STEP_SIZE = 50

def is_on_screen(a_window, the_turtle):
    '''Returns True if the_turtle is within the bounds of
       a_window.'''
    left_side = a_window.window_width() / -2
    right_side = a_window.window_width() / 2
    top_side = a_window.window_height() / 2
    bottom_side = a_window.window_height() / -2
    
    turtle_x = the_turtle.xcor()
    turtle_y = the_turtle.ycor()
      
    return turtle_x < right_side and turtle_x > left_side and turtle_y < top_side and turtle_y > bottom_side

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

henry = turtle.Turtle()
henry.shape("turtle")
henry.pensize(3)

while is_on_screen(canvas, henry):
    choice = random.randrange(0, 3)
    if choice == 0:
        henry.left(90)
    elif choice == 1:
        henry.right(90)
    #if it's a 2, don't turn at all
        
    henry.forward(STEP_SIZE)
    

print("Off the screen...")
    
    