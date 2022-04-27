def sum_to(n):
    # initialize the variable
    total = 0
    
    # repeatedly update the value of the variable
    for counter in range(n+1):
        total = total + counter
    
    return total

print(sum_to(1000000000))