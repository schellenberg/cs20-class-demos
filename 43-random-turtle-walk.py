import turtle
import random

def is_on_screen(window, a_turtle):
    left_edge = -(window.window_width()/2)
    right_edge = window.window_width()/2
    top_edge = window.window_height()/2
    bottom_edge = -(window.window_height()/2)
    
    x = a_turtle.xcor()
    y = a_turtle.ycor()
    
    if x > left_edge and x < right_edge and y < top_edge and y > bottom_edge:
        return True
    else:
        return False

canvas = turtle.Screen()
john = turtle.Turtle()
john.shape("turtle")

while is_on_screen(canvas, john):
    choice = random.randrange(0, 3)
    if choice == 0: #forward
        john.forward(50)
    elif choice == 1: #left
        john.left(90)
        john.forward(50)
    else: #right
        john.right(90)
        john.forward(50)

print("All done!")