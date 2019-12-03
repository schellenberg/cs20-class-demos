def remove_vowels(some_string):
    vowels = "aeiouyAEIOUY"
    string_without_vowels = ""
    for letter in some_string:
        if letter not in vowels:
            string_without_vowels = string_without_vowels + letter
    return string_without_vowels

print(remove_vowels("Walter Murray Collegiate Institute"))
print(remove_vowels("Marauders"))
print(remove_vowels("Saskatoon Saskatchewan"))