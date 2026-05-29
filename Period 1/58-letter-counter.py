import requests

alphabet = "abcdefghijklmnopqrstuvwxyz"
url = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
text = str(requests.get(url).content)

def letter_count(text, letter_to_find):
    '''Prints out the percentage of the text that is letter_to_find.'''
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
    letter_count(text, letter)
    
