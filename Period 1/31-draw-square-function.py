import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, with each side being side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)


window = turtle.Screen()
window.bgcolor("lightgreen")

john = turtle.Turtle()
john.shape("turtle")
john.pensize(5)

tj = turtle.Turtle()
tj.color("blue")
tj.shape("turtle")

draw_square(john, 100)
draw_square(tj, 300)




