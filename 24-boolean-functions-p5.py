def is_divisible(first_number, second_number):
    if first_number % second_number == 0:
        return True
    else:
        return False


print(is_divisible(48, 5)) #false
print(is_divisible(50, 5)) #true