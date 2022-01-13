def vowel_killer(some_string):
    vowels = "aeiouyAEIOUY"
    new_string = ""
    for letter in some_string:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string
    
#Walter Murray ---> Wltr Mrr
print(vowel_killer("Walter Murray"))