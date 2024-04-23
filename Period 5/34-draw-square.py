import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each
       side is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
window = turtle.Screen()
luc = turtle.Turtle()
luc.color("blue")
caylixx = turtle.Turtle()
caylixx.color("darkred")

draw_square(luc, 200)
caylixx.backward(250)
draw_square(caylixx, 75)

