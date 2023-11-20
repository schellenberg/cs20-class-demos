import turtle
import random

def is_in_screen(the_window, the_turtle):
    left_side = -(the_window.window_width() / 2)
    right_side = the_window.window_width() / 2
    top_side = the_window.window_height() / 2
    bottom_side = -(the_window.window_height() / 2)
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    still_in = True
    if x < left_side or x > right_side:
        still_in = False
    if y < bottom_side or y > top_side:
        still_in = False
    
    return still_in

canvas = turtle.Screen()
wyatt = turtle.Turtle()
wyatt.shape("turtle")
wyatt.pensize(5)

while is_in_screen(canvas, wyatt):
    coin = random.randrange(0, 2)
    
    if coin == 0: #heads
        wyatt.left(90)
    else: #tails
        wyatt.right(90)
    
    wyatt.forward(50)
    