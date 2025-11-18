def multiply(number1, number2):
    # initialize variable
    total = 0
    # repeat
    for counter in range(number1):
        # change variable
        total = total + number2
    return total

print(multiply(5, 7))