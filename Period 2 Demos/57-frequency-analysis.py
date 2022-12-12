import requests

url = "https://www.gutenberg.org/cache/epub/145/pg145.txt"
text = str(requests.get(url).content)

def count(text, letter_to_find):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    
    number_of_letter = 0
    total_letters = 0
    for letter in text:
        if letter in alphabet:
            total_letters = total_letters + 1
        if letter == letter_to_find:
            number_of_letter = number_of_letter + 1
    percent = number_of_letter / total_letters * 100
    percent = round(percent, 2)
    print(f"Letter: {letter_to_find}  Percentage: {percent}")
    
    
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count(text, letter)

