import turtle

def draw_rectangle(a_turtle, width, height):
    '''a_turtle -> turtle.Turtle() object
       width -> integer
       height -> integer
       
       Draw a rectangle, where you end facing the same
       direction that you started.'''
    for side in [width, height, width, height]:
        a_turtle.forward(side)
        a_turtle.left(90)

canvas = turtle.Screen()
joel = turtle.Turtle()
joel.pensize(5)

for rectangle in range(4):
    draw_rectangle(joel, 150, 75)
    joel.left(90)
    