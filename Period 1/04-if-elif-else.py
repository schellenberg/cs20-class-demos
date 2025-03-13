#ask user for the temperature
temperature = input("What's the temperature? ")
temperature = int(temperature)

#if the temp is less than -15, tell them to wear a parka
if temperature < -15:
    print("Wear a parka!")
