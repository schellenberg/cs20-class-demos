import turtle
import random

STEP_SIZE = 25

def is_on_screen(the_turtle, some_screen):
    '''Returns True if the the_turtle is inside the bounds
       of some_screen. False otherwise.'''
    left = some_screen.window_width()/-2
    right = some_screen.window_width()/2
    top = some_screen.window_height()/2
    bottom = some_screen.window_height()/-2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    return x > left and x < right and y > bottom and y < top


canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

garrett = turtle.Turtle()
garrett.shape("turtle")
garrett.pensize(3)


while is_on_screen(garrett, canvas):
    choice = random.randrange(0, 3)
    if choice == 0:
        garrett.left(90)
    elif choice == 1:
        garrett.right(90)
    #if it's a 2, don't do anything...
    garrett.forward(STEP_SIZE)

print("Off the screen!")



