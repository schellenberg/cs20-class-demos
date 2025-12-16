import requests

def calculate_percent(text, letter_to_find):
    '''Prints the percentage of text that is the
       letter_to_find.'''
    count = 0
    total_letters = 0
    for letter in text.lower():
        if letter in alphabet:
            total_letters += 1
        if letter == letter_to_find:
            count += 1
    percentage = (count/total_letters) * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")

the_url = "https://www.gutenberg.org/cache/epub/46/pg46.txt"
the_text = str(requests.get(the_url).content)
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    calculate_percent(the_text, letter)

