import turtle

def draw_rectangle(a_turtle, width, height):
    '''a_turtle -> turtle.Turtle() object
       width -> integer
       height -> integer
       
       Draw a rectangle, ending in the same spot you started,
       facing the same direction.'''
    for side in [width, height, width, height]:
        a_turtle.forward(side)
        a_turtle.left(90)

window = turtle.Screen()
erika = turtle.Turtle()
erika.pensize(5)

for rectangle in range(8):
    draw_rectangle(erika, 150, 50)
    erika.left(90)
    erika.forward(50)
    erika.right(90)
    erika.left(360/8)
