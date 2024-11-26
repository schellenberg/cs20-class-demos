def is_cold(temperature):
    '''Returns True if it's cold. False otherwise.'''
    return temperature < -20
#     if temperature < -20:
#         return True
#     else:
#         return False
    
current_temp = input("What's the temperature? ")
current_temp = float(current_temp)

if is_cold(current_temp):
    print("Brrrr.....")
else:
    print("I'm doing okay!")
    