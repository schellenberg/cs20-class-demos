def square_root(number):
    # initialize the variable
    guess = number / 2
    
    # repeatedly update the value of the variable
    for counter in range(6):
        guess = 0.5 * (guess + number/guess)
    
    return guess

print(square_root(25))

