# Car Gas Usage
# Sept 28, 2020

# taking user input
distance = input("How far did you drive (in km)? " )
gas_used = input("How much gas did you use (in L)? ")

# converted input to a number
distance = float(distance)
gas_used = float(gas_used)

# do the math
answer = gas_used / distance * 100
answer = round(answer, 2)

# printed the result
print("Your car used", answer, "L/100km")