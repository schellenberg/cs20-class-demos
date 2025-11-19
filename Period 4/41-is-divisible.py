def is_divisible(the_number, divisor):
    if the_number % divisor == 0:
        return True
    else:
        return False

print(is_divisible(15, 4))