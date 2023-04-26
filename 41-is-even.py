def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

the_number = 0
while is_even(the_number):
    the_number = input("What's the number? ")
    the_number = int(the_number)

