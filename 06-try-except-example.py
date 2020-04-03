
number = input("Please enter your favorite number: ")

try:
    number = int(number)
    distance_from_42 = abs(42 - number)
    print(f"Your favorite number is {distance_from_42} away from 42")
    
except:
    print("Woah. Please enter an integer!")