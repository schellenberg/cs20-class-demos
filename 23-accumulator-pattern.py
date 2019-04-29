def sum_to_n(highest_number):
#    #accumulator pattern version
#    the_sum = 0
#    for counter in range(1, highest_number + 1):
#        the_sum = the_sum + counter

    #gauss version...
    the_sum = highest_number*(highest_number+1)/2
    return the_sum

print( sum_to_n(10000000000) )
