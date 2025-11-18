# def sum_to(number):
#     the_sum = 0
#     for counter in range(1, number + 1):
#         the_sum = the_sum + counter
#     return the_sum

def sum_to(number):
    return number * (number + 1) / 2

print(sum_to(1000000000))