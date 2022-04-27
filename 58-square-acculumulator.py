def square(some_number):
    # accumulator pattern
    #initialize a variable
    total = 0    

    #repeatedly, update that value
    for counter in range(some_number):
        total = total + some_number
    
    return total

print(square(3))