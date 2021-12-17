import turtle
import time

window = turtle.Screen()

weather = ""

while True:
    with open("weather.txt") as data:
        weather = data.readline().strip()
    
    if weather == "bloody cold":
        window.bgcolor("cyan")
    elif weather == "hot":
        window.bgcolor("red")
