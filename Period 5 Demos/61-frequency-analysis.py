import requests

the_url = "https://www.gutenberg.org/cache/epub/46/pg46.txt"
the_text = str(requests.get(the_url).content)

def count_letters(text, letter_to_find):
    '''Counts how many times letter_to_find is in the text.'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    times_seen = 0
    total_letters = 0
    text = text.lower()  #don't miss the capitals...
    for letter in text:
        if letter in alphabet:
            total_letters += 1
            if letter == letter_to_find:
                times_seen = times_seen + 1
            
    percentage = (times_seen/total_letters) * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} showed up {percentage}%")


alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count_letters(the_text, letter)

