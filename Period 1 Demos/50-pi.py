def my_pi():
    #initialize
    pi = 0
    is_adding = True
    #repeat
    for denominator in range(1, 100000, 2):
        #change value
        if is_adding:
            pi = pi + 1/denominator
        else:
            pi = pi - 1/denominator
        
        is_adding = not is_adding
    
    pi = pi * 4
    return pi

print(my_pi())