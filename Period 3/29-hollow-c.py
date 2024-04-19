import turtle

window = turtle.Screen()

drake = turtle.Turtle()
drake.pensize(5)

#an option, but not the best
# drake.forward(150)
# drake.left(90)
# drake.forward(20)
# drake.left(90)
# drake.forward(130)
# drake.right(90)
# drake.forward(110)
# drake.right(90)
# drake.forward(130)
# drake.left(90)
# drake.forward(20)
# drake.left(90)
# drake.forward(150)
# drake.left(90)
# drake.forward(150)
# drake.left(90)

#better option!
# for length in [20, 100, 100, 100, 20, 80]:
#     drake.right(90)
#     drake.forward(length)
#     
# for length in [60, 80]:
#     drake.left(90)
#     drake.forward(length)


#another option
# for c in [250, 50, 300, 300, 300, 50, 250]:
#     drake.forward(c)
#     drake.right(90)
# 
# drake.backward(200)


#best option
# for i in [100, -100, 20, -80, -60, -80, 20, -100]:
#     drake.right(90)
#     drake.forward(i)
    
#one more way
for side in [250, 50, 300, 300, 300, 50, 250, 0, 0, 200]:
    drake.forward(side)
    drake.right(90)
