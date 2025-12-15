def vowel_killer(some_string):
    '''Return some_string will all vowels removed.'''
    new_string = ""
    vowels = "aeiouyAEIOUY"
    for letter in some_string:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string

# print(vowel_killer("apple"))
# print(vowel_killer("computer science"))
print(vowel_killer("Walter Murray Collegiate"))