import turtle
import random

def is_inside_screen(the_screen, the_turtle):
    left = the_screen.window_width()/-2
    right = the_screen.window_width()/2
    top = the_screen.window_height()/2
    bottom = the_screen.window_height()/-2
    
    x = the_turtle.xcor()
    y = the_turtle.ycor()
    
    if x > left and x < right and y < top and y > bottom:
        return True
    else:
        return False

canvas = turtle.Screen()
natasha = turtle.Turtle()
natasha.shape("turtle")
natasha.speed(0)

while is_inside_screen(canvas, natasha):
    choice = random.randrange(0, 3)
    if choice == 0:
        natasha.left(90)
    elif choice == 1:
        natasha.right(90)
    #don't turn if it's a 2 as the choice
    natasha.forward(20)
    
print("Off the screen! Stopping now!")