def square(the_number):
    the_answer = the_number * the_number
    return the_answer

some_number = input("What number should we square? ")
some_number = int(some_number)
result = square(some_number)
print(f"The square of {some_number} is {result}")