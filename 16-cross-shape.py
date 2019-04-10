import turtle

def cross_shape(some_turtle, side_length):
    """Draws a cross shape with a given turtle and side length.
       
       some_turtle: a turtle.Turtle() object
       side_length: a number representing the length of each side
    """
    for u_shape in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)

def draw_square(my_turtle, length_of_side):
    """Draws a square with a turtle and a given side length.

       my_turtle: a turtle.Turtle() object
       length_of_side: number representing length of every side
    """
    for side in range(4):
        my_turtle.forward(length_of_side)
        my_turtle.left(90)


window = turtle.Screen()

sage = turtle.Turtle()
sage.pensize(4)

emerson = turtle.Turtle()
emerson.color("blue")
emerson.pensize(6)

#cross_shape(sage, 75)
#cross_shape(emerson, 150)
draw_square(emerson, 100)

