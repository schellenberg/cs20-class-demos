def sum_to(n):
    total = 0
    for counter in range(1, n+1):
        total = total + counter
    return total

print(sum_to(100))