import turtle

def draw_square(my_turtle, length_of_side):
    """Draws a square with a turtle and a given side length.

       my_turtle: a turtle.Turtle() object
       length_of_side: number representing length of every side
    """
    for side in range(4):
        my_turtle.forward(length_of_side)
        my_turtle.right(90)

def draw_square_from_center(my_turtle, side_length):
    """Draws a square from the center point of the square, and ends at that same location.
       
       my_turtle: a turtle.Turtle() object
       side_length: number representing length of every side
    """

    # getting to starting location
    my_turtle.penup()
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.pendown()
    
    draw_square(my_turtle, side_length)
    
    #go back to starting point in center
    my_turtle.penup()
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.forward(side_length/2)
    my_turtle.right(90)
    my_turtle.pendown()


canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

abrar = turtle.Turtle()
abrar.pensize(4)
#abrar.speed(1)
draw_square_from_center(abrar, 150)
abrar.left(45)
draw_square_from_center(abrar, 150)
