import requests

url = "https://www.gutenberg.org/files/84/84-0.txt"
book = str(requests.get(url).content)
book = book.lower()

the_alphabet = "abcdefghijklmnopqrstuvwxyz"

def frequency_of(some_letter, text):
    total_letters = 0
    number_of_the_letter = 0
    for letter in text:
        if letter in the_alphabet:
            total_letters += 1
        if letter == some_letter:
            number_of_the_letter += 1

    return number_of_the_letter / total_letters * 100

for letter in the_alphabet:
    print(letter, frequency_of(letter, book))