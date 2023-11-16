import turtle

def draw_rectangle(a_turtle, length, width):
    '''Draw a rectangle with a_turtle, starting with side length
       long, then the width length long.'''
    for side_length in [length, width, length, width]:
        a_turtle.forward(side_length)
        a_turtle.left(90)
        
def draw_mutated_cog(some_turtle, short_side, long_side, number_of_rectangles):
    '''Draws what Broden tells us is a mutated cog, using some_turtle. It's really
       just a bunch of rectangles in a circle...'''
    for rectangle in range(number_of_rectangles):
        draw_rectangle(some_turtle, long_side, short_side)
        some_turtle.left(90)
        some_turtle.forward(short_side)
        some_turtle.right(90)
        some_turtle.left(360/number_of_rectangles)

canvas = turtle.Screen()
karthik = turtle.Turtle()
karthik.pensize(3)
karthik.speed(0)

draw_mutated_cog(karthik, 50, 150, 8)
