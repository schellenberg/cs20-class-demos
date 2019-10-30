import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with the given turtle, with
       each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(360/4)

# setting up window and turtles
canvas = turtle.Screen()
iftemum = turtle.Turtle()
iftemum.shape("turtle")
iftemum.pensize(5)

sam = turtle.Turtle()
sam.shape("circle")
sam.color("yellow")
sam.pensize(10)

#drawing
draw_square(iftemum, 300)
draw_square(sam, 150)