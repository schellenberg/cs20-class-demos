import requests

url = "https://www.gutenberg.org/cache/epub/100/pg100.txt"
text = str(requests.get(url).content)

def count(text, letter_to_find):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    times_letter_seen = 0
    total_letters = 0
    text = text.lower()
    
    for letter in text:
        if letter in alphabet:
            total_letters = total_letters + 1
        if letter == letter_to_find:
            times_letter_seen = times_letter_seen + 1
    
    percent = times_letter_seen / total_letters * 100
    percent = round(percent, 2)
    print(f"Letter: {letter_to_find}  Percent: {percent}")


alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count(text, letter)

