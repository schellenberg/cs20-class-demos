temp = input("What is the temperature?")
temp = int(temp)

if temp < -10:
    print("Wear a parka")
elif temp < 10:
    print("Wear a sweater")
else:
    print("Wear a t-shirt")