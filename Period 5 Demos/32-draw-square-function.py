import turtle

def draw_square(some_turtle, side_length):
    '''Draws a square with some_turtle, where each side is side_length long.'''
    for side in range(4):
        some_turtle.forward(side_length)
        some_turtle.left(90)
        
def draw_cross(some_turtle, side_length):
    '''Draws a cross shape with some_turtle, where each side is side_length long.'''
    for i in 4 * [270, 90, 90]:
        some_turtle.left(i)
        some_turtle.forward(side_length)
        
        
window = turtle.Screen()
joti = turtle.Turtle()
joti.color("red")

william = turtle.Turtle()
william.color("blue")

#draw_square(joti, 150)
#draw_square(william, 250)

draw_cross(joti, 100)
