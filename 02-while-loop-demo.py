keep_going = True

while keep_going:
    name = input("Who are you? ")
    
    if name == "Dan":
        keep_going = False

print("Hello there, " + name)