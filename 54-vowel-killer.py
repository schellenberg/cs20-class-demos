def vowel_killer(some_string):
    '''Returns some_string, but with all the vowels removed.'''
    
    vowels = "aeiouyAEIOUY"
    #initialize value
    no_vowels_string = ""
    #repeat
    for letter in some_string:
        #update value
        if letter not in vowels:
            no_vowels_string = no_vowels_string + letter
    return no_vowels_string
            
            
# compsci -> cmpsc
print(vowel_killer("compsci"))
# walter murray -> wltr mrr
print(vowel_killer("walter murray"))