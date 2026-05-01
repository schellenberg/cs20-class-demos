import turtle
import random

def still_on_screen(the_window, the_turtle):
    '''Returns true if the_turtle is within the_window.
       False if it's off the edge.'''
    left = -the_window.window_width()/2
    right = the_window.window_width()/2
    top = the_window.window_height()/2
    bottom = -the_window.window_height()/2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    return x > left and x < right and y < top and y > bottom
    

canvas = turtle.Screen()
kabeer = turtle.Turtle()
kabeer.shape("turtle")
kabeer.color("blue")
kabeer.pensize(3)
kabeer.speed(0)

while still_on_screen(canvas, kabeer):
    choice = random.randrange(0, 3)
    if choice == 0:
        kabeer.left(90)
    if choice == 1:
        kabeer.right(90)
    
    kabeer.forward(10)
        
print("I'm off the screen!")