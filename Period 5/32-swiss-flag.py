import turtle

canvas = turtle.Screen()
harsimran = turtle.Turtle()
harsimran.pensize(5)

#riley's solution
for cross in range(4):
    for rl in [90, 270, 90]:
        harsimran.forward(100)
        harsimran.right(rl)

#michael's solution
# for repeat in range(2):
#     for side in [100, 100, 100, -100, -100, -100]:
#         harsimran.forward(side)
#         harsimran.right(90)
       
#sajid's solution
# for side in range(4):
#     harsimran.forward(50)
#     harsimran.right(90)
#     harsimran.forward(50)
#     harsimran.right(90)
#     harsimran.forward(50)
#     harsimran.left(90)

