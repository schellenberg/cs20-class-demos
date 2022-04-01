import turtle

canvas = turtle.Screen()

aj = turtle.Turtle()
aj.pensize(5)

#slightly adapted from Andrew
for distance in [100, 25, 125, 150, 125, 25, 100, 0, 0, 100]:
    aj.forward(distance)
    aj.right(90)

#Andrew's solution
# for distance in [100, 25, 125, 150, 125, 25, 100]:
#     aj.forward(distance)
#     aj.right(90)
# aj.left(180)
# aj.forward(100)


# Victor's solution

# for i in range(2):
#     for j in [80, 20, 80]:
#         aj.forward(j)
#         aj.left(90)
#     
#     if i == 0:
#         aj.left(180)
#         aj.forward(60)
#         aj.right(90)
# 
# aj.right(90)
# for k in [20, 100, 20]:
#     aj.forward(k)
#     aj.left(90)