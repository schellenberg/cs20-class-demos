def square(the_number):
    answer = the_number * the_number
    return answer


some_number = input("What number do you want to square?")
some_number = int(some_number)
result = square(some_number)
print(result)