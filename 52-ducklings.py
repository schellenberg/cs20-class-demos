prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "Q" or letter == "O":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
