import turtle

def draw_square(my_turtle, side_length):
    '''my_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draws a square with the given turtle,
       with each side side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_inner_square(a_turtle, smaller_square_size, buffer_distance):
    '''a_turtle -> turtle.Turtle() object
       smaller_square_size -> integer
       buffer_distance -> integer
       
       Draws two squares, one inside the other. The inside square
       has side lengths of smaller_square_size, and the distance
       between the squares is buffer_distance.'''
    draw_square(a_turtle, smaller_square_size)
    a_turtle.penup()
    a_turtle.backward(buffer_distance)
    a_turtle.right(90)
    a_turtle.forward(buffer_distance)
    a_turtle.left(90)
    a_turtle.pendown()
    draw_square(a_turtle, smaller_square_size + buffer_distance*2)


screen = turtle.Screen()
al = turtle.Turtle()
al.pensize(5)

draw_inner_square(al, 200, 50)

