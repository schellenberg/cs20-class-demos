def vowel_killer(the_string):
    '''Returns the_string with vowels removed.'''
    new_string = ""
    for letter in the_string:
        if letter not in "aeiouAEIOU":
            new_string = new_string + letter
    return new_string
    

print(vowel_killer("walter murray"))
print(vowel_killer("sunshine would be nice"))