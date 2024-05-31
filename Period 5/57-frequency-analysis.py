import requests

def letter_counter(the_text, letter_to_find):
    '''Prints out the percentage of letter_to_find out of
       all letters in the_text.'''
    
    the_text = the_text.lower() #catch upper case as well
    times_letter_was_seen = 0
    total_letters = 0
    for letter in the_text:
        if letter in alphabet:
            total_letters += 1
            if letter == letter_to_find:
                times_letter_was_seen += 1
    percentage = (times_letter_was_seen / total_letters) * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")
    
the_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
book = str(requests.get(the_url).content)
    
alphabet = "abcdefghijklmnopqrstuvwxyz"
for some_letter in alphabet:
    letter_counter(book, some_letter)


