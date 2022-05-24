def vowel_killer(word):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter not in vowels:
            result = result + letter
    return result

print("walter murray")
print(vowel_killer("walter murray"))