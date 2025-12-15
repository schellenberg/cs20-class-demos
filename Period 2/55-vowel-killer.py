def vowel_killer(some_string):
    '''Returns some_string with all vowels removed.'''
    vowels = "aeiouAEIOU"
    new_string = ""
    for letter in some_string:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string

print(vowel_killer("apple"))
print(vowel_killer("computer science"))
print(vowel_killer("walter murray collegiate"))