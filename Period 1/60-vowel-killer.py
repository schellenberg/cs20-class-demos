def vowel_killer(word):
    '''Returns the word with all vowels removed.'''
    new_string = ""
    for letter in word:
        if letter not in "aeiouAEIOU":
            new_string = new_string + letter
    return new_string

print(vowel_killer("walter murray"))
print(vowel_killer("computer science"))
