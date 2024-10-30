import turtle

the_window = turtle.Screen()
the_window.bgcolor("orange")

zaynah = turtle.Turtle()
zaynah.shape("turtle")
zaynah.color("blue")
zaynah.pensize(5)

ben = turtle.Turtle()
ben.shape("turtle")
ben.color("green")
ben.pensize(10)

ben.penup()
ben.backward(200)
ben.pendown()

#make ben draw a square
for side in range(4):
    ben.forward(100)
    ben.left(90)

# draw me a pentagon  -- 5 sides
for side in range(5):
    zaynah.forward(100)
    zaynah.left(360/5)
    
the_window.exitonclick()