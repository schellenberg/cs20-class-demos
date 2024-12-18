def vowel_killer(word):
    '''Returns the word, with all the vowels removed.'''
    the_vowels = "aeiouyAEIOUY"
    
    # initialize variable
    no_vowel_string = ""
    # repeat
    for letter in word:
        # update the variable
        if letter not in the_vowels:
            no_vowel_string += letter

    return no_vowel_string

print(vowel_killer("Walter Murray"))