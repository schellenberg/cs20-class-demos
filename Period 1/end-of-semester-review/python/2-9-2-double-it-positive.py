def double_it_positive(the_number):
    # Positive numbers are doubled.
    if the_number > 0:
        return the_number * 2
    # Zero stays zero.
    elif the_number == 0:
        return 0
    # Negative numbers get the special answer -1 instead of being doubled.
    else:
        return -1