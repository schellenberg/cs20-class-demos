import requests

the_url = "https://www.gutenberg.org/files/2600/2600-0.txt"
book = str(requests.get(the_url).content)
book = book.lower() #makes every letter into lowercase

alphabet = "abcdefghijklmnopqrstuvwxyz"
for character in alphabet:
    total_counter = 0
    letter_counter = 0
    for letter in book:
        if letter == character:
            letter_counter += 1
        if letter in alphabet:
            total_counter += 1

    percentage = round( (letter_counter / total_counter) * 100 , 2)
    #print(total_counter, letter_counter, percentage)
    print(f'The letter {character} makes up {percentage}% of the characters in this text.')