import turtle

def draw_square(my_turtle, side_length):
    '''my_turtle -> turtle.Turtle() object
       side_length -> int
    
       Draws a square, starting and ending in the bottom left corner.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_square_from_center(some_turtle, side_length):
    '''some_turtle -> turtle.Turtle() object
       side_length -> int
       
       Draws a square, starting and ending in the middle of the square.'''
    #go to bottom left corner
    some_turtle.penup()
    some_turtle.backward(side_length/2)
    some_turtle.right(90)
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.pendown()
    
    #draw square
    draw_square(some_turtle, side_length)

    #head back to center
    some_turtle.penup()
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
    some_turtle.right(90)
    some_turtle.pendown()
    
window = turtle.Screen()
ayman = turtle.Turtle()
ayman.pensize(5)

draw_square_from_center(ayman, 300)
ayman.left(45)
draw_square_from_center(ayman, 300)