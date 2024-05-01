def square(number):
    the_square = number ** 2
    return the_square

the_number = input("What number should we square? ")
the_number = int(the_number)
answer = square(the_number)
print(f"The square of {the_number} is {answer}")