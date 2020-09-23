temp = input("What's the temp outside? ")
temp = int(temp)

if temp < -10:
    print("wear a toque")

elif temp < 15:
    print("wear a long sleeve shirt")

else:
    print("wear a t-shirt")