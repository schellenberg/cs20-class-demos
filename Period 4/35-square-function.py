# def hello():
#     print("Hello world!")
# 
# hello()

# import math
# print(math.pow(2, 3))

def square(the_number):
    '''Sends back the square of the_number.'''
    the_square = the_number * the_number
    return the_square

number = input("What number should I square? ")
number = int(number)
result = square(number)
print(f"The square of {number} is {result}.")
# print(the_square)
