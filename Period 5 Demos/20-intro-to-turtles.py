import turtle

#setup window and turtle
canvas = turtle.Screen()
jessica = turtle.Turtle()

#draw shape
#naive method
# jessica.forward(150)
# jessica.left(90)
# jessica.forward(150)
# jessica.left(90)
# jessica.forward(150)
# jessica.left(90)
# jessica.forward(150)
# jessica.left(90)

#while loop
# side = 0
# while side < 4:
#     jessica.forward(150)
#     jessica.left(90)
#     side = side + 1
    
#for loop
for side in range(4):
    jessica.forward(150)
    jessica.left(90)


