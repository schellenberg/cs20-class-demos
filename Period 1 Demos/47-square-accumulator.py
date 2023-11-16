def square(original_number):
    #initialize
    total = 0
    #repeat
    for counter in range(original_number):
        #change value
        total = total + original_number
    
    return total

to_square = input("What should we square? ")
to_square = int(to_square)
result = square(to_square)
print(f"The square of {to_square} is {result}")