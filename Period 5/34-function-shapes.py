import turtle

def draw_cross(some_turtle, side_length):
    '''Draws a cross shape with some_turtle.
       Every side is side_length long.'''
    for u_shape in range(4):
        for angle in [-90, -90, 90]:
            some_turtle.forward(side_length)
            some_turtle.left(angle)
    
    
def draw_c(a_turtle, longest_side_length, width_of_c):
    '''Draws a hollow c shape. The size is determined by the longest_side_length.
       Calculates the smaller sides using width_of_c.'''
    s = width_of_c
    m = longest_side_length - width_of_c
    l = longest_side_length
    end = longest_side_length - width_of_c * 2

    for distance in [m, s, l, l, l, s, m, -end]:
        a_turtle.forward(distance)
        a_turtle.left(90)
    

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

thy = turtle.Turtle()
thy.color("red")
thy.pensize(5)

# draw_cross(thy, 50)
draw_c(thy, 300, 75)
