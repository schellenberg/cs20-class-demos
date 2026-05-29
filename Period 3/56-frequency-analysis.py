import requests

url = "https://www.gutenberg.org/cache/epub/2554/pg2554.txt"
text = str(requests.get(url).content)
alphabet = "abcdefghijklmnopqrstuvwxyz"

def letter_counter(text, letter_to_find):
    '''Returns the percentage of letter_to_find in text.'''
    counter = 0
    total_letters = 0
    for letter in text.lower():
        if letter in alphabet:
            total_letters = total_letters + 1
        if letter == letter_to_find:
            counter = counter + 1
    percentage = counter / total_letters * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")

for letter in alphabet:
    letter_counter(text, letter)

