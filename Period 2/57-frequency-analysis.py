import requests

def count(the_text, letter_to_find):
    '''Prints the percentage of the_text that is
       the letter_to_find.'''
    counter = 0
    total_letters = 0
    for letter in the_text.lower():
        if letter in alphabet:
            total_letters += 1
        if letter == letter_to_find:
            counter += 1
    percentage = (counter / total_letters) * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")

the_url = "https://www.gutenberg.org/cache/epub/46/pg46.txt"
my_text = str(requests.get(the_url).content)
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count(my_text, letter)

