def check_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True
    
number_to_check = input("What number should we check? ")
number_to_check = int(number_to_check)
print(check_odd(number_to_check))