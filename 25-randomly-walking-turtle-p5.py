import turtle
import random

canvas = turtle.Screen()

logan = turtle.Turtle()
logan.color("magenta")
logan.pensize(4)
logan.shape("turtle")

def flip_coin_and_move(some_turtle):
    total = random.randrange(1,3)
    if total == 1:
        some_turtle.left(90)
    else:
        some_turtle.right(90)
    some_turtle.forward(50)

def still_inside_screen(some_screen, some_turtle):
    top = 1/2 * some_screen.window_height()
    bottom = -1/2 * some_screen.window_height()
    right = 1/2 * some_screen.window_width()
    left = -1/2 * some_screen.window_width()
    
    x = some_turtle.xcor()
    y = some_turtle.ycor()
    
    still_in = True
    if x <= left or x >= right:
        still_in = False
    if y >= top or y <= bottom:
        still_in = False
    
    return still_in

while still_inside_screen(canvas, logan):
    flip_coin_and_move(logan)