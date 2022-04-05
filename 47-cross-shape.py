import turtle

canvas = turtle.Screen()
saad = turtle.Turtle()

#Aidan T Solution
saad.right(90)
for rep in range(4):
    saad.forward(100)
    saad.left(90)
    saad.forward(100)
    saad.right(90)
    saad.forward(100)
    saad.left(90)

# Nini and Angela's Solution
# for shape in range(4):
#     for side in [100, 100, 100, 0, 0]:
#         saad.forward(side)
#         saad.right(90)

# Aidan's Solution
# for side in range(12):
#     saad.forward(50)
#     if side == 2 or side == 5 or side == 8 or side == 11:
#         saad.right(90)
#     else:
#         saad.left(90)

# Schellenberg's Solution
# for u_shape in range(4):
#     for side in range(3):
#         saad.forward(100)
#         saad.left(90)
#     saad.left(180)
