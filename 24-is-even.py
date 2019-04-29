def is_even(number):
    return number % 2 == 0

def is_divisible(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False

print(is_divisible(10, 5))