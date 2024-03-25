got_password_right = False

while got_password_right == False:
    password = input("What's the password? ")
    
    if password == "waltermurray":
        got_password_right = True
        
    else:
        print("That's not it! Try again!")
        

print("What a great place to be!")