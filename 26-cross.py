import turtle

def draw_cross(a_turtle, side_length):
    '''Draws a cross / Switzerland flag using a_turtle, where each side is side_length long.'''
    #Monica's version
    for counter in range(4):
        for side in range(3):
            a_turtle.forward(side_length)
            a_turtle.left(90)
        a_turtle.right(180)


#setup window and turtle
window = turtle.Screen()
kayaan = turtle.Turtle()

draw_cross(kayaan, 100)

# Ben's version:
# for counter in range(12): 
#     kayaan.right(90)
#     if counter % 3 == 0:
#         kayaan.forward(100)
#     else:
#         kayaan.forward(-100)