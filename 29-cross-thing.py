import turtle

def draw_cross(a_turtle, length_of_side):
    '''Draws a cross shape, with each side being length_of_side long.'''
    for counter in range(4):
        for turn in [90, 90, 270]:
            a_turtle.forward(length_of_side)
            a_turtle.left(turn)

window = turtle.Screen()

esther = turtle.Turtle()
esther.color("green")
esther.shape("turtle")

draw_cross(esther, 50)
