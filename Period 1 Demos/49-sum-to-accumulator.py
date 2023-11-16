def sum_to(number):
    #accumulator pattern method
    #initialize
    total = 0
    #repeat
    for counter in range(1, number + 1):
        #change value
        total = total + counter
    
    #gauss was a genius method
#     total = number * (number + 1) / 2
    return total


print(sum_to(100))
    

