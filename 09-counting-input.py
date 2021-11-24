# get user input
small_number = input("What's the small number? ")
large_number = input("What's the large number? ")

# convert to integers
small_number = int(small_number)
large_number = int(large_number)

for number in range(small_number, large_number+1):
    print(number)
    