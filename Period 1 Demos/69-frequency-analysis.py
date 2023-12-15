import requests

the_url = "https://www.gutenberg.org/cache/epub/46/pg46.txt"
the_text = str(requests.get(the_url).content)

def count_letters(text, letter):
    '''Return the percentage that letter shows up in text.'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    total_letters = 0
    times_seen = 0
    for character in text.lower():  #turn everything to lowercase
        if character in alphabet:
            total_letters = total_letters + 1
            if character == letter:
                times_seen = times_seen + 1
    
    percentage = (times_seen/total_letters) * 100
    percentage = round(percentage, 2)
    
    print(f"{letter} shows up {percentage}%")


alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count_letters(the_text, letter)

