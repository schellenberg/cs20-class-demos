import turtle

def draw_cross(a_turtle, side_length):
    '''a_turtle -> turtle.Turtle() object
       side_length -> int
       
       Draw a cross/Swiss flag shape.'''
    for u_shape in range(4):
        for side in range(3):
            a_turtle.forward(side_length)
            a_turtle.left(90)
        a_turtle.left(180)

def draw_square(some_turtle, side_length):
    '''some_turtle -> turtle.Turtle() object
       side_length -> int
       
       Draw a square with the given turtle and side length.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)

window = turtle.Screen()
victor = turtle.Turtle()
victor.pensize(5)

draw_square(victor, 100)

#schellenberg's solution
# for u_shape in range(4):
#     for side in range(3):
#         victor.forward(100)
#         victor.left(90)
#     victor.left(180)

#maurya's solution
# for side in [50, 50, 50, -50, 0, 0, 50, 50, -50, 0, 0, 50, 50, -50, 0, 0, 50, 50]:
#     victor.forward(side)
#     victor.left(90)

#dhanush's solution
# for x in range(4):
#     victor.forward(100)
#     victor.left(90)
#     victor.forward(100)
#     victor.right(90)
#     victor.forward(100)
#     victor.right(90)

# hyder's solution
# for side in range(4):
#     for size in range(2):
#         victor.forward(100)
#         victor.right(90)
#     victor.forward(100)
#     victor.left(90)
