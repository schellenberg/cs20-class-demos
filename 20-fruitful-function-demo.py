def find_average(first, second, third):
    the_sum = first + second + third
    average = the_sum / 3
    return average

def my_abs(some_number):
    if some_number < 0:
        some_number = some_number * -1
    return some_number

print(my_abs(6))