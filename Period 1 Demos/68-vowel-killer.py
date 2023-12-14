def vowel_killer(some_string):
    vowels = "aeiouAEIOU"
    no_vowels_string = ""
    for letter in some_string:
        if letter not in vowels:
            no_vowels_string = no_vowels_string + letter
    return no_vowels_string

the_string = input("What should I remove vowels from? ")
print(vowel_killer(the_string))