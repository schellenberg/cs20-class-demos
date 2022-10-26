counter = 100
while counter != 1:
    if counter % 2 == 0:
        counter = counter / 2
    else:
        counter = counter * 3 + 1
    
    print(counter)
    