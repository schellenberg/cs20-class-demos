def remove_vowels(some_string):
    vowels = "aeiouyAEIOUY"
    no_vowels_string = ""
    
    for letter in some_string:
        if letter not in vowels:
            no_vowels_string = no_vowels_string + letter
    
    return no_vowels_string

print(remove_vowels("amaad is always saying yes"))
print(remove_vowels("Walter Murray Collegiate Institute"))
