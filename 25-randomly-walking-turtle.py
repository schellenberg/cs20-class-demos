import random
import turtle

window = turtle.Screen()

corey = turtle.Turtle()
corey.color("purple")
corey.pensize(4)
corey.shape("turtle")

def random_turn(some_turtle):
#     movement = ["left", "right"]
#     move = random.choice(movement)
    the_choice = random.randrange(1, 101)
    if the_choice < 50:
        some_turtle.left(90)
    else:
        some_turtle.right(90)

def is_in_the_screen(some_window, some_turtle):
    top = some_window.window_height() / 2
    bottom = -(some_window.window_height() / 2)
    right = some_window.window_width() / 2
    left = -(some_window.window_width() / 2)
    
    x = some_turtle.xcor()
    y = some_turtle.ycor()
    
    still_in = True
    if x < left or x > right:
        still_in = False
    if y < bottom or y > top:
        still_in = False
    
    return still_in
    

while is_in_the_screen(window, corey):
    random_turn(corey)
    corey.forward(75)
    
    