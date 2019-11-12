def sum_to(n):
    # initialize a variable
    total = 0
    
    for counter in range(1, n+1):
        # change the value of the variable
        total = total + counter
    return total 

def my_sqrt(n):
    guess = n / 2
    for counter in range(15):
        guess = 0.5 * (guess + n / guess)
    return guess


def estimate_pi():
    quarter_pi = 0
    is_adding = True
    for denominator in range(1, 1000000, 2):
        if is_adding:
            quarter_pi = quarter_pi + 1 / denominator
            is_adding = False
        else:
            quarter_pi = quarter_pi - 1 / denominator
            is_adding = True
            
    return quarter_pi * 4

print(estimate_pi())