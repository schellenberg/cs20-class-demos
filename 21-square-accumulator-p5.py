def square(number):
    total = 0
    for counter in range(number):
        total = total + number
    return total

thing_to_square = 3
the_answer = square(thing_to_square)
print(f"The square of {thing_to_square} is {the_answer}.")