import turtle

canvas = turtle.Screen()
uwais = turtle.Turtle()

lengths = [200, 75, 275, 300, 275, 75, 200]
for side in lengths:
    uwais.forward(side)
    uwais.right(90)

uwais.left(180)
uwais.forward(150)
