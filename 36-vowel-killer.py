def vowel_killer(some_string):
    vowels = "aeiouyAEIOUY"
    no_vowel_string = ""
    for letter in some_string:
        if letter not in vowels:
            no_vowel_string = no_vowel_string + letter
    return no_vowel_string

print(vowel_killer("Walter Murray Collegiate"))