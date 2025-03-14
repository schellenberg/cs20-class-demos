def say_hello(name):
    # say hi to Vedika or Mary. Anyone else, say Go away!
    if name == "Vedika":
        print("Hi there, " + name)
    elif name == "Mary":
        print("Hi there, " + name)
    else:
        print("Go away, " + name)
    
say_hello("Vedika")
say_hello("Mary")
say_hello("Graham")