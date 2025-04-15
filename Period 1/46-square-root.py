def square_root(some_number, number_of_guesses):
    #initialize variable
    guess = some_number / 2
    #repeat
    for counter in range(number_of_guesses):
        #adjust variable
        guess = 0.5 * (guess + (some_number / guess))
    
    return guess

print(square_root(9, 5))