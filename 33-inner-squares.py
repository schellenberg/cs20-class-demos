import turtle

def draw_square(my_turtle, side_length):
    '''my_turtle -> turtle.Turtle() object
       side_length -> int
    
       Draws a square, starting and ending in the bottom left corner.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_inner_squares(some_turtle, inner_side_length, buffer_length):
    '''some_turtle -> turtle.Turtle() object
       inner_side_length -> int
       buffer_length -> int
       
       Draws two squares, with the smaller one having side lengths of
       inner_side_length, and the distance between the squares being
       buffer_length.'''
    draw_square(some_turtle, inner_side_length)
    some_turtle.penup()
    some_turtle.backward(buffer_length)
    some_turtle.right(90)
    some_turtle.forward(buffer_length)
    some_turtle.left(90)
    some_turtle.pendown()
    draw_square(some_turtle, inner_side_length + buffer_length*2)

window = turtle.Screen()
window.bgcolor("lightgreen")

sadia = turtle.Turtle()
sadia.pensize(5)
sadia.shape("turtle")

draw_inner_squares(sadia, 150, 20)

