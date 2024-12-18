def vowel_killer(word):
    '''Returns the word, with all the vowels removed.'''
    vowels = "aeiouAEIOU"
    #initialize a variable
    no_vowel_string = ""

    #repeat
    for letter in word:
        #change the variable
        if letter not in vowels:
            no_vowel_string = no_vowel_string + letter
    
    return no_vowel_string

print(vowel_killer("Walter Murray"))