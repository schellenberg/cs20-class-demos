import requests

def letter_count(the_text, letter_to_find):
    '''Print the percentage of letters that are
       in the_text.'''
    times_seen = 0
    total_letters = 0
    the_text = the_text.lower() #get rid of capital letters
    for letter in the_text:
        if letter in alphabet:
            total_letters += 1
        if letter == letter_to_find:
            times_seen += 1
    
    percentage = (times_seen / total_letters) * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")

alphabet = "abcdefghijklmnopqrstuvwxyz"

the_url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
book = str(requests.get(the_url).content)

for some_letter in alphabet:
    letter_count(book, some_letter)




