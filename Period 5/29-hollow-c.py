import turtle

window = turtle.Screen()
adam = turtle.Turtle()
adam.pensize(5)

#spewing code version
# adam.forward(180)
# adam.left(90)
# adam.forward(20)
# adam.left(90)
# adam.forward(200)
# adam.left(90)
# adam.forward(200)
# adam.left(90)
# adam.forward(200)
# adam.left(90)
# adam.forward(20)
# adam.left(90)
# adam.forward(180)
# adam.right(90)
# adam.forward(160)
# adam.right(90)


#chase's version -- way better!
# for hollow_c in [180, 20, 200, 200, 200, 20, 180]:
#     adam.forward(hollow_c)
#     adam.left(90)
# 
# adam.right(180)
# adam.forward(160)

#michael's adaptation
for hollow_c in [180, 20, 200, 200, 200, 20, 180, -160]:
    adam.forward(hollow_c)
    adam.left(90)
    
    
