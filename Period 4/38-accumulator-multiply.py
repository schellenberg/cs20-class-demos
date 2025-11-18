def multiply(number1, number2):
    product = 0
    for counter in range(number1):
        product = product + number2
    return product

print(multiply(3, 6))