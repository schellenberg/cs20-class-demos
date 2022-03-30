import turtle

#create screen to draw on
window = turtle.Screen()
window.bgcolor("black")

#make turtle to draw with
nini = turtle.Turtle()
nini.color("pink")
nini.shape("turtle")
nini.pensize(10)

hermann = turtle.Turtle()
hermann.color("red")
hermann.pensize(4)

#draw a triangle
for side in range(3):
    nini.forward(100)
    nini.left(120)

#hermann draws a pentagon
for side in range(5):
    hermann.forward(200)
    hermann.left(360/5)
