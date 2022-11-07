import turtle

def draw_cross(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draws a cross shape, with the given size.'''
    for u_shape in range(4):
        for side in range(3):
            a_turtle.forward(side_length)
            a_turtle.left(90)

        a_turtle.left(180)

def draw_square(the_turtle, side_length):
    '''the_turtle -> turtle.Turtle() object
       side_length -> integer
       
       Draw a square, with each side side_length long.'''
    for side in range(4):
        the_turtle.forward(side_length)
        the_turtle.left(90)

window = turtle.Screen()
alexandra = turtle.Turtle()
alexandra.pensize(4)

hanson = turtle.Turtle()
hanson.pensize(10)
hanson.color("red")

# draw_cross(alexandra, 50)
# draw_cross(hanson, 100)

draw_square(hanson, 200)