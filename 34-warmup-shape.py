import turtle

def draw_rectangle(some_turtle, length, width):
    '''Draw a rectangle with the given turtle, length and width.'''
    for side in range(2):
        some_turtle.forward(length)
        some_turtle.left(90)
        some_turtle.forward(width)
        some_turtle.left(90)
    
def draw_starburst(a_turtle, length, width):
    '''Draw 8 rectangles, with an octagon in the middle.'''
    for rectangle in range(8):
        draw_rectangle(a_turtle, length, width)
        a_turtle.left(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.left(360/8)

canvas = turtle.Screen()
caleb = turtle.Turtle()

draw_starburst(caleb, 100, 20)
