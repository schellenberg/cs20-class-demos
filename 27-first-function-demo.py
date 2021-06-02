import turtle

def draw_square(some_turtle, side_length):
    '''Use some_turtle to draw a square of side_length size.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(360/4)


window = turtle.Screen()
aaron = turtle.Turtle()

son = turtle.Turtle()
son.color("blue")
son.penup()
son.backward(200)
son.pendown()

draw_square(aaron, 50)
draw_square(son, 150)
