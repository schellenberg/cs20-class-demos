import turtle

window = turtle.Screen()
radia = turtle.Turtle()
radia.pensize(5)

# nested for loop solution
# for u_shape in range(4):
#     for side in range(3):
#         radia.forward(100)
#         radia.left(90)
#     radia.left(180)

#radia's solution
# for side in range(4):
#     radia.forward(100)
#     radia.left(90)
#     radia.forward(100)
#     radia.right(90)
#     radia.forward(100)
#     radia.right(90)

#quan's solution
# for angle in [90, 90, -90] * 4:
#     radia.forward(150)
#     radia.left(angle)

#andgadveer's solution
# for i in range(12):
#     radia.forward(100)
#     if i == 2 or i == 5 or i == 8 or i == 11:
#         radia.right(90)
#     else:
#         radia.left(90)