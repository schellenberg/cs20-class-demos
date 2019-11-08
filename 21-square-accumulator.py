def square(number):
    total = 0
    for counter in range(number):
        total = total + number
    return total

to_square = 3
result = square(to_square)
print(f"If you square {to_square}, you get {result}.")