import requests

def letter_count(text, letter_to_find):
    '''Prints out the percentage of letters that are letter_to_find in text.'''
    letter_seen = 0
    total_letters = 0
    text = text.lower() #won't miss capital letters
    for letter in text:
        if letter in alphabet:
            total_letters += 1
        if letter == letter_to_find:
            letter_seen += 1
    percentage = letter_seen / total_letters * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")
    

alphabet = "abcdefghijklmnopqrstuvwxyz"
# phrase = "Good afternoon!"

url = "https://www.gutenberg.org/cache/epub/100/pg100.txt"
the_text = str(requests.get(url).content)

for letter in alphabet:
    letter_count(the_text, letter)
    

