import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, with each side is
       length is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
        
window = turtle.Screen()
isen = turtle.Turtle()
marie = turtle.Turtle()
marie.color("pink")

draw_square(isen, 200)
marie.backward(300)
draw_square(marie, 75)
draw_square(marie, 150)
