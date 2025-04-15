def square_root(some_number, guesses):
    # initialize variable
    root = some_number/2
    # repeat
    for the_guess in range(guesses):
        # adjust the variable
        root = 0.5 * (root + (some_number / root))
    
    return root

print(square_root(64, 7))