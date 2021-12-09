import turtle

def draw_rectangle(a_turtle, small_side, long_side):
    '''Draws a rectangle with a given turtle,
       ending in the same orientation as it starts.'''
    for side in [long_side, small_side, long_side, small_side]:
        a_turtle.forward(side)
        a_turtle.left(90)

window = turtle.Screen()
moiz = turtle.Turtle()

for shape in range(4):
    draw_rectangle(moiz, 75, 200)
    moiz.left(90)


