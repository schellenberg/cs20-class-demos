import turtle

def draw_triangle(a_turtle, side_length):
    '''Draws a triangle using a_turtle, with each side
       being side_length long.'''
    for side in range(3):
        a_turtle.forward(side_length)
        a_turtle.left(360/3)


window = turtle.Screen()
gunjan = turtle.Turtle()
gunjan.pensize(5)

for triangle in range(6):
    draw_triangle(gunjan, 200)
    gunjan.left(360/6)
