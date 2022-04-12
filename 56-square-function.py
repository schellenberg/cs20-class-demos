def square_number(some_number):
    '''Returns the square of a number.'''
    answer = some_number ** 2
    return answer

user_number = int(input("What number should we use?"))
square = square_number(user_number)
print(f"The square of {user_number} is {square}")