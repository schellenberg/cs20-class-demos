#ask the user for the temperature
temperature = input("What's the temperature? ")
temperature = float(temperature)

#if the temp is less than -15, tell them to wear a parka
if temperature < -15:
    print("Wear a parka!")

elif temperature < 0:
    print("Wear a sweater!")

elif temperature < 15:
    print("Wear a t-shirt!")

else:
    print("Wear shorts!")