temperature = input("What's the temperature? ")
temperature = int(temperature)

if temperature > 15:
    print("Wear a t-shirt")
elif temperature > 0:
    print("Wear a sweater")
else:
    print("Wear a jacket")