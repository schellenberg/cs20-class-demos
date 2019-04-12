import random

def a(number):
    print("A: Some message", number)

def b(number):
    print("B: A different message", number*2)

def c(number):
    print("C: Yet another message", number*3)

things = [a, b, c]
random.choice(things)(5)