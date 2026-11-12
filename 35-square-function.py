import turtle

def draw_square(some_turtle, side_length, the_color):
    '''Draws a square with some_turtle, where each side is side_length long,
       and the lines are the_color.'''
    some_turtle.color(the_color)
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

#setup window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup turtles
parker = turtle.Turtle()
parker.shape("turtle")

himal = turtle.Turtle()

draw_square(parker, 200, "blue")
draw_square(himal, 350, "red")
