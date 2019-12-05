import requests

url = "https://www.gutenberg.org/files/1661/1661-0.txt"
book = str(requests.get(url).content)
book = book.lower()

the_alphabet = "abcdefghijklmnopqrstuvwxyz"

def find_frequency_of(letter_to_find, text_to_search):
    number_of_letter = 0
    total_letters = 0
    for letter in text_to_search:
        if letter in the_alphabet:
            total_letters = total_letters + 1
            if letter == letter_to_find:
                number_of_letter = number_of_letter + 1
    
    return number_of_letter / total_letters * 100

for letter in the_alphabet:
    print(letter, find_frequency_of(letter, book))





