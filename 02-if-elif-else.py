temp = input("What's the temperature? ")
temp = int(temp)

if temp < -10:
    print("Wear a jacket!")
elif temp < 0:
    print("Wear a sweater!")
elif temp < 15:
    print("Wear pants.")
else:
    print("Wear shorts!")