def is_cold(temperature):
    return temperature < -20

#     if temperature < -20:
#         return True
#     else:
#         return False
    
how_cold = input("What's the temperature? ")
how_cold = float(how_cold)

if is_cold(how_cold):
    print("Brrr....")
else:
    print("I'm okay!")