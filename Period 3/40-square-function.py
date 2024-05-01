def square(some_number):
    the_square = some_number * some_number
    return the_square


number_to_square = input("What number should we square? ")
number_to_square = int(number_to_square)
answer = square(number_to_square)
print(f"The square of {number_to_square} is {answer}")