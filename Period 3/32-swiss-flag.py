import turtle

canvas = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(5)

#jacob's method
# for shape in range(4):
#     alex.forward(150)
#     alex.right(90)
#     alex.forward(150)
#     alex.right(90)
#     alex.forward(150)
#     alex.left(90)

#isen's method
# for times in range(4):
#     for angle in [90, 90, -90]:
#         alex.forward(150)
#         alex.left(angle)
        
        
#amy's method
# for times in range(4):
#     for side_length in [-100, 100, 100]:
#         alex.right(90)
#         alex.forward(side_length)


#sumaiya's method
for side in [100, 100, 100, 0, 0, 100, 100, 100, 0, 0, 100, 100, 100, 0, 0, 100, 100, 100]:
    alex.forward(side)
    alex.left(90)
        

