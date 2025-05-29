def qwerty_finder(word):
    for index in range(len(word)):
        letter = word[index]
        if letter in "qwerty":
            return index
    return -1

