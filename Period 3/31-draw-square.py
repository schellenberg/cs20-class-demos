import turtle

def draw_square(a_turtle, side_length):
    '''Draws a square with a_turtle, where each side
       is side_length long.'''
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)
        
canvas = turtle.Screen()
david = turtle.Turtle()
tian = turtle.Turtle()
tian.color("red")
tian.pensize(2)

draw_square(david, 200)
draw_square(david, 100)
draw_square(tian, 300)
