# def hello():
#     print("Hello World!")
#     
# 
# hello()

# import math
# print(math.pow(2, 3))

def square(some_number):
    '''Sends back the square of some_number.'''
    the_square = some_number * some_number
    return the_square

number = input("What number should I square? ")
number = int(number)
result = square(number)
print(f"The square of {number} is {result}.")
#print(the_square)


