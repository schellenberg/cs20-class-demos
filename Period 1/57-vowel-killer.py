def vowel_killer(some_string):
    '''Returns some_string, but with all vowels removed.'''
    vowels = "aeiouAEIOU"
    new_string = ""
    for letter in some_string:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string

print(vowel_killer("Walter Murray"))
print(vowel_killer("Computer Science 20"))