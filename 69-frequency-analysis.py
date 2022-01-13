import requests

url = "https://www.gutenberg.org/files/1661/1661-0.txt"
page = requests.get(url)
the_text = str(page.content)

def count(the_letter, text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    number_of_letter = 0
    total_letters = 0
    
    for letter in text:
        if letter.lower() in alphabet:
            total_letters += 1
        if letter.lower() == the_letter:
            number_of_letter += 1
    
    percent = (number_of_letter / total_letters) * 100
    rounded_percent = round(percent, 2)
    print(f"{the_letter}: {rounded_percent}% -- {number_of_letter} / {total_letters}")

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count(letter, the_text)
