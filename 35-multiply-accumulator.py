def multiply(first_number, second_number):
    '''Multiply these values together, using accumulation.'''
    answer = 0                           #initialize accumulator
    for step in range(first_number):     #repeat
        answer = answer + second_number     #accumulate
    return answer                        #return final result
    
def square(some_number):
    '''Squares a number using accumulation'''
    total = 0
    for counter in range(some_number):
        total = total + some_number
    return total
    
def sum_to(the_number):
    '''Adds up all the numbers from 1 to the_number.'''
    answer = 0
    for counter in range(the_number + 1):
        answer = answer + counter
    return answer

    #using the gauss pattern...
    #return (the_number * (the_number+1)) / 2
    
    
def my_sqrt(n, number_of_guesses):
    '''Estimate the square root of n, by repeating number_of_guesses times'''
    guess = n/2
    for counter in range(number_of_guesses):
        guess = 0.5 * (guess + n / guess)
    return guess
    
print(my_sqrt(12, 7))