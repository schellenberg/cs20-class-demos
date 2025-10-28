import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

yasin = turtle.Turtle()
yasin.shape("turtle")

#version one
# yasin.forward(200)
# yasin.left(90)
# yasin.forward(30)
# yasin.left(90)
# yasin.forward(170)
# yasin.right(90)
# yasin.forward(140)
# yasin.right(90)
# yasin.forward(170)
# yasin.left(90)
# yasin.forward(30)
# yasin.left(90)
# yasin.forward(200)
# yasin.left(90)
# yasin.forward(200)
# yasin.left(90)



#version two
# yasin.forward(170)
# yasin.left(90)
# yasin.forward(30)
# yasin.left(90)
# yasin.forward(200)
# yasin.left(90)
# yasin.forward(200)
# yasin.left(90)
# yasin.forward(200)
# yasin.left(90)
# yasin.forward(30)
# yasin.left(90)
# yasin.forward(170)
# yasin.right(90)
# yasin.forward(140)
# yasin.right(90)


# #version three
# for step in [170, 30, 200, 200, 200, 30]:
#     yasin.forward(step)
#     yasin.left(90)
#     
# for step in [170, 140]:
#     yasin.forward(step)
#     yasin.right(90)
    

#version four
for step in [170, 30, 200, 200, 200, 30, 170, -140]:
    yasin.forward(step)
    yasin.left(90)
    