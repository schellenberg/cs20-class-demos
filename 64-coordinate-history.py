import turtle
import random

canvas = turtle.Screen()
emma = turtle.Turtle()
emma.pensize(5)

history = [[0, 0]]
still_moving = True

while still_moving:
    choice = random.randrange(1, 101)
    if choice < 33:
        emma.left(90)
    elif choice < 66:
        emma.right(90)
    #no else required, since we just go forward...
        
    emma.forward(10)
    
    x = round(emma.xcor())
    y = round(emma.ycor())
    current_location = [x, y]
    
    if current_location in history:
        still_moving = False
        print(history)
        
    else:
        history.append(current_location)
    
