def square(number):
    '''Returns the square of the number.'''
    #initialize variable
    total = 0
    
    #repeat
    for times in range(number):
        #change variable
        total = total + number
    
    return total

answer = square(6)
print(answer)