import turtle

screen = turtle.Screen()

nikita = turtle.Turtle()
nikita.pensize(5)

#one method
# nikita.forward(160)
# nikita.right(90)
# nikita.forward(40)
# nikita.right(90)
# nikita.forward(200)
# nikita.right(90)
# nikita.forward(200)
# nikita.right(90)
# nikita.forward(200)
# nikita.right(90)
# nikita.forward(40)
# nikita.right(90)
# nikita.forward(160)
# nikita.left(90)
# nikita.forward(120)


#better method
# for side in [160, 40, 200, 200, 200, 40, 160]:
#     nikita.forward(side)
#     nikita.right(90)
# 
# nikita.left(180)
# nikita.forward(120)


#best method
# for side in [160, 40, 200, 200, 200, 40, 160, 0, 0, 120]:
#     nikita.forward(side)
#     nikita.right(90)

#bestest method
for side in [160, 40, 200, 200, 200, 40, 160, -120]:
    nikita.forward(side)
    nikita.right(90)

