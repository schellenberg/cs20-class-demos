import turtle

window = turtle.Screen()
danny = turtle.Turtle()
danny.pensize(5)

#basic version
# danny.forward(100)
# danny.left(90)
# danny.forward(20)
# danny.left(90)
# danny.forward(120)
# danny.left(90)
# danny.forward(120)
# danny.left(90)
# danny.forward(120)
# danny.left(90)
# danny.forward(20)
# danny.left(90)
# danny.forward(100)
# danny.left(90)
# danny.forward(-80)
# danny.left(90)

#better version
for side_length in [100, 20, 120, 120, 120, 20, 100, -80]:
    danny.forward(side_length)
    danny.left(90)
    
    