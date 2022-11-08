import turtle

def draw_square(my_turtle, side_length):
    '''my_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draws a square with the given turtle, with
       each side being side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_inner_square(a_turtle, length_of_small_square, buffer_distance):
    '''a_turtle -> turtle.Turtle() object
       length_of_small_square -> integer
       buffer_distance -> integer
       
       Draws two squares, one inside the other. The smaller square will
       have a side length of length_of_small_square, and the gap between
       them will be buffer_distance long.'''
    draw_square(a_turtle, length_of_small_square)
    a_turtle.penup()
    a_turtle.backward(buffer_distance)
    a_turtle.right(90)
    a_turtle.forward(buffer_distance)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, length_of_small_square + buffer_distance*2)

screen = turtle.Screen()
aaraiz = turtle.Turtle()
aaraiz.pensize(5)

draw_inner_square(aaraiz, 250, 50)

