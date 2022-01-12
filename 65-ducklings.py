prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        letter = letter + "u"
    print(letter + suffix)
