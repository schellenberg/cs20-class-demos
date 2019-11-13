def estimate_pi():
    quarter_pi = 0
    is_adding = True
    for denominator in range(1, 1000000000, 2):
        if is_adding == True:
            quarter_pi = quarter_pi + 1 / denominator
            is_adding = False
        else:
            quarter_pi = quarter_pi - 1 / denominator
            is_adding = True
    
    return quarter_pi * 4

print(estimate_pi())