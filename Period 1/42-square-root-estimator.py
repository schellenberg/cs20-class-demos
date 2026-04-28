def my_sqrt(n, number_of_guesses):
    '''Estimates a square root using Newton's algorithm.'''
    #initialize accumulator
    root = n/2
    #repeat
    for counter in range(number_of_guesses):
        #change accumulator
        root = 0.5 * (root + (n/root))
    return root

answer = my_sqrt(16, 6)
print(answer)
            