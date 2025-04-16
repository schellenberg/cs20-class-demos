import turtle
import random

def is_within_screen(the_window, the_turtle):
    left = the_window.window_width() / -2
    right = the_window.window_width() / 2
    top = the_window.window_height() / 2
    bottom = the_window.window_height() / -2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    if x > left and x < right and y > bottom and y < top:
        return True
    else:
        return False

canvas = turtle.Screen()
rylan = turtle.Turtle()
rylan.shape("turtle")
rylan.speed(0)

while is_within_screen(canvas, rylan):
    choice = random.randrange(0, 3)
    if choice == 0:
        rylan.left(90)
    elif choice == 1:
        rylan.right(90)
    #if it's a 2, don't turn
    rylan.forward(20)

print("I'm off the screen! Stopping now!")