import turtle
import random

def is_on_screen(the_window, the_turtle):
    left_side = -the_window.window_width()/2
    right_side = the_window.window_width()/2
    top_side = the_window.window_height()/2
    bottom_side = -the_window.window_height()/2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    if x > right_side or x < left_side:
        return False
    elif y > top_side or y < bottom_side:
        return False
    else:
        return True 
    

canvas = turtle.Screen()
duncan = turtle.Turtle()
duncan.shape("turtle")
duncan.pensize(5)
duncan.speed(8)

while is_on_screen(canvas, duncan):
    coin = random.randrange(0, 2)
    if coin == 0:   #heads
        duncan.left(90)
    else:   #tails
        duncan.right(90)
    
    duncan.forward(50)

print("Bah! I hit the edge!")
canvas.exitonclick()