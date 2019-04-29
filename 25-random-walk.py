import turtle
import random

def is_inside_screen(the_turtle, the_window):
    top = the_window.window_height() / 2
    bottom = -(the_window.window_height() / 2)
    right = the_window.window_width() / 2
    left = -(the_window.window_width() / 2)
    
    turtle_x = the_turtle.xcor()
    turtle_y = the_turtle.ycor()
    
    still_in = True
    # check left/right
    if turtle_x > right or turtle_x < left:
        still_in = False
    
    if turtle_y > top or turtle_y < bottom:
        still_in = False
    
    return still_in
    

canvas = turtle.Screen()
anu = turtle.Turtle()

while is_inside_screen(anu, canvas):
    anu.forward(75)
    coin = random.randrange(0, 2)
    if coin == 0:
        anu.left(90)
    else:
        anu.right(90)