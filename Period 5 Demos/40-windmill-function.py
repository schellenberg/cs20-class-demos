import turtle

def draw_rectangle(a_turtle, width, height):
    '''a_turtle -> turtle.Turtle() object
       width -> integer
       height -> integer
       
       Draw a rectangle, ending facing the same
       direction you started, in the same spot.'''
    for side in [width, height, width, height]:
        a_turtle.forward(side)
        a_turtle.left(90)

window = turtle.Screen()
wasi = turtle.Turtle()
wasi.pensize(4)

for rectangle in range(8):
    draw_rectangle(wasi, 200, 50)
    wasi.left(90)
    wasi.forward(50)
    wasi.right(90)
    wasi.left(360/8)
    
