the_sentence = "Walter Murray Collegiate"
vowels = "aeiouy"

#accumulator pattern
new_sentence = ""
for letter in the_sentence:
    if letter not in vowels:
        new_sentence = new_sentence + letter

print(new_sentence)