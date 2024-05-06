def square(number):
    '''Returns the square of the number.'''
    #initialize variable
    total = 0
    #repeat
    for loop in range(number):
        #changing variable
        total = total + number
    return total

answer = square(4)
print(answer)