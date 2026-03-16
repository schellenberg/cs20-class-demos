#get info from user
temperature = input("What is the temperature? ")

#convert data types
temperature = int(temperature)

#output clothing suggestion
if temperature < -5:
    print("Wear a jacket!")
elif temperature < 10:
    print("Wear a sweater!")
elif temperature < 20:
    print("Wear a t-shirt!")
else:
    print("Wear shorts!")