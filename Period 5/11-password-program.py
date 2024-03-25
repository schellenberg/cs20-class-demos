got_password_right = False

while got_password_right == False:
    password = input("What's the password? ")
    
    if password == "madness":
        got_password_right = True

    else:
        print("Whoops. That's not it. Try again!")

print("I'm getting crushed in March Madness. But it's fun!")  