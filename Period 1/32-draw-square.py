import turtle

def draw_square(my_turtle, side_length):
    '''Draws a square with my_turtle, where each side is
       side_length long.'''
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)
    

window = turtle.Screen()
eric = turtle.Turtle()
musa = turtle.Turtle()
musa.color("red")
musa.pensize(2)

draw_square(eric, 200)
draw_square(eric, 100)
draw_square(musa, 300)
