def cube(number):
    '''Returns the cube of the number passed in.'''
    answer = number * number * number
    return answer

original_number = 3
result = cube(original_number)
print(f"The cube of {original_number} is {result}.")
