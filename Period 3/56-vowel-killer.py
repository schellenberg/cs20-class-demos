def vowel_killer(some_string):
    '''Returns some_string, but with all vowels removed.'''
    no_vowels_string = ""
    vowels = "aeiouAEIOU"
    for letter in some_string:
        if letter not in vowels:
            no_vowels_string = no_vowels_string + letter
    return no_vowels_string

print(vowel_killer("Walter Murray Collegiate"))