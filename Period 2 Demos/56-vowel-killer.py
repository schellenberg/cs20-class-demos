def vowel_killer(the_word):
    # initialize
    word_without_vowels = ""

    # repeat
    for letter in the_word:
        # accumulate
        vowels = "aeiouAEIOU"
        if letter not in vowels:
            word_without_vowels = word_without_vowels + letter
        
    return word_without_vowels


print(vowel_killer("walter murray collegiate"))
print(vowel_killer("evan hardy"))
