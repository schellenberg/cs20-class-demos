import turtle

def draw_cross(some_turtle, side_length):
    '''some_turtle -> turtle.Turtle() object
       side_length -> an integer
       
       Draws a cross shape with the given size.'''
    for u_shape in range(4):
        for side in range(3):
            some_turtle.forward(side_length)
            some_turtle.left(90)
        some_turtle.left(180)


def draw_square(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> an integer
       
       Draws a square, with each side side_length long.'''
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)

window = turtle.Screen()
ben = turtle.Turtle()
ben.pensize(5)

anamol = turtle.Turtle()
anamol.color("red")
anamol.pensize(3)

draw_square(ben, 200)
draw_cross(anamol, 100)

