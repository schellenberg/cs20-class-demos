import requests

def letter_count(the_text, letter_to_find):
    '''Print the percentage of letters that are letters_to_find
       in the_text.'''
    
    the_text = the_text.lower() #force every character to lowercase
    times_letter_seen = 0
    total_letters = 0
    for letter in the_text:
        if letter in alphabet:
            total_letters += 1
            if letter == letter_to_find:
                times_letter_seen += 1

    percentage = (times_letter_seen / total_letters) * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")


the_url = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"
book = str(requests.get(the_url).content)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for some_letter in alphabet:
    letter_count(book, some_letter)
    

