import turtle
import random

def still_in_screen(the_window, the_turtle):
    '''Returns True if the_turtle is within the_window.
       False if it falls off the edge.'''
    left = the_window.window_width()/-2
    right = the_window.window_width()/2
    top = the_window.window_height()/2
    bottom = the_window.window_height()/-2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    return x > left and x < right and y < top and y > bottom

canvas = turtle.Screen()
narayan = turtle.Turtle()
narayan.shape("turtle")
narayan.color("green")
narayan.pensize(3)
narayan.speed(0)
# canvas.tracer(2)

while still_in_screen(canvas, narayan):
    movement = ["left", "right", "forward"]
    move = random.choice(movement)
    if move == "left":
        narayan.left(90)
    if move == "right":
        narayan.right(90)
    
    narayan.forward(15)
    
print("I'm off the screen!")
        
        