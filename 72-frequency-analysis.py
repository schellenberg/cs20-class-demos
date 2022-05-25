import requests

def letter_count(letter, text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    letter_count = 0
    total_letters = 0
    
    for character in text:
        if character in alphabet:
            total_letters += 1
            if character.lower() == letter:
                letter_count += 1
    
    percent = (letter_count / total_letters) * 100
    percent = round(percent, 2)
    print(f"{letter} - {percent}% of the text")

def frequency_analysis(text):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letter_count(letter, text)

#sherlock holmes
book_url = "https://www.gutenberg.org/files/1661/1661-0.txt"
text = str(requests.get(book_url).content)
frequency_analysis(text)



