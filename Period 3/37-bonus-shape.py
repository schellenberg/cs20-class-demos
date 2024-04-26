#bonus question

import turtle

def draw_square_from_middle_of_side(some_turtle, side_length):
    '''Draws a square, starting and ending in the middle of one of
       the side lengths.'''
    some_turtle.forward(side_length/2)
    for side in range(3):
        some_turtle.left(90)
        some_turtle.forward(side_length)
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
        

window = turtle.Screen()
chisom = turtle.Turtle()
chisom.pensize(5)

for square in range(5):
    draw_square_from_middle_of_side(chisom, 200)
    chisom.left(360/5)
    
    