
def sum_to(number):
    #initialilze
    total = 0

    #repeat
    for counter in range(number + 1):
        #modify
        total = total + counter
    return total


print(sum_to(10))
