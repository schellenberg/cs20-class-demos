import turtle

def draw_weird_square(a_turtle, side_length):
    '''Draw a strange square shape with a_turtle,
       where each segment is side_length long.'''
    for side in range(8):
        a_turtle.forward(side_length)
        a_turtle.right(45)
        a_turtle.forward(side_length)
        a_turtle.left(90)

screen = turtle.Screen()
kevin = turtle.Turtle()
kevin.shape("turtle")
kevin.pensize(5)

draw_weird_square(kevin, 75)

# khan-vinh's version
# for side in range(4):
#     for angle in [45, 270, 45, 0]:
#         kevin.forward(50)
#         kevin.right(angle)
#     kevin.left(90)

#schellenberg's version


