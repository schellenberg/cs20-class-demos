def is_divisible_by_2(some_number):
    return some_number % 2 == 0
    
def is_divisible_by(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False
    
num = 8
print(is_divisible_by(num, 4))