def vowel_killer(original_string):
    #initialize
    new_string = ""

    #repeat
    vowels = "aeiouAEIOU"
    for letter in original_string:
        #accumulate
        if letter not in vowels:
            new_string = new_string + letter

    return new_string

print(vowel_killer("walter murray collegiate"))
print(vowel_killer("San Antonio Spurs"))
print(vowel_killer("David Robinson"))
