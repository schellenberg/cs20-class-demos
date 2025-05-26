import turtle

def draw_string(some_turtle, shape, length, angle):
    '''Draws the shape using some_turtle.
       F: forward
       -: left
       +: right'''
    for letter in shape:
        if letter == "F":
            some_turtle.forward(length)
        elif letter == "+":
            some_turtle.right(angle)
        elif letter == "-":
            some_turtle.left(angle)
    

canvas = turtle.Screen()
aidan = turtle.Turtle()
aidan.shape("turtle")

shape = 'FFFF--FF--FFFF--FF'
draw_string(aidan, shape, 50, 45)
