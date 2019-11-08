def sum_to(number):
    total = 0
    for counter in range(1, number+1):
        total = total + counter
    return total


the_answer = sum_to(100)
print(f"The sum is {the_answer}.")
