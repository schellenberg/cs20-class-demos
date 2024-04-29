import turtle

def draw_triangle(my_turtle, side_length):
    '''Draws a triangle with my_turtle, where each side
       is side_length long.'''
    for side in range(3):
        my_turtle.forward(side_length)
        my_turtle.left(360/3)
        

canvas = turtle.Screen()
ella = turtle.Turtle()
ella.pensize(5)

for triangle in range(6):
    draw_triangle(ella, 200)
    ella.left(360/6)

