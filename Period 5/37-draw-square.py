import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side
       is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")

arbe = turtle.Turtle()
arbe.pensize(3)

john = turtle.Turtle()
john.color("red")
john.pensize(3)

draw_square(arbe, 200)
draw_square(john, 150)







