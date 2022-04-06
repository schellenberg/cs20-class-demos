import turtle

def draw_cross(some_turtle, side_length):
    '''Draw a red cross looking shape with the given turtle
       and given side_length.'''
    
    # Nini and Angela's Solution
    for shape in range(4):
        for side in [side_length, side_length, side_length, 0, 0]:
            some_turtle.forward(side)
            some_turtle.right(90)


canvas = turtle.Screen()
saad = turtle.Turtle()

draw_cross(saad, 25)



