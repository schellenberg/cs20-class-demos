import turtle

def draw_mulicolor_square(some_turtle, side_length):
    '''Use some_turtle to draw a multi-colored square, with each side being side_length long.'''
    for side_color in ["red", "blue", "yellow", "purple"]:
        some_turtle.color(side_color)
        some_turtle.forward(side_length)
        some_turtle.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

alec = turtle.Turtle()
alec.pensize(3)
alec.speed(0)

size = 20
for counter in range(15):
    draw_mulicolor_square(alec, size)
    size = size + 10
    alec.forward(10)
    alec.right(18)
