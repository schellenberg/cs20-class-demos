def vowel_killer(some_string):
    '''Returns the string with all the vowels removed.'''
    vowels = "aeiouAEIOU"
    no_vowel_string = ""
    for letter in some_string:
        if letter not in vowels:
            no_vowel_string = no_vowel_string + letter
    return no_vowel_string

phrase = input("What should I kill vowels from? ")
print(vowel_killer(phrase))