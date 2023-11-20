def my_pi():
    #initialize
    quarter_pi = 0
    is_adding = True
    #repeat
    for denominator in range(1, 1000000, 2):
        #change value
        if is_adding == True:
            quarter_pi = quarter_pi + 1/denominator
        else:
            quarter_pi = quarter_pi - 1/denominator
        
        is_adding = not is_adding
    
    return quarter_pi * 4

print(my_pi())