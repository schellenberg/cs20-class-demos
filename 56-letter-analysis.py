#frequency analysis
import requests

def count_letter(text, letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    total_letters = 0
    found_letters = 0
    for char in text.lower():
        if char in alphabet:
            total_letters += 1  #total_letters = total_letters + 1
            if char == letter:
                found_letters += 1
    
    percent = (found_letters / total_letters) * 100
    rounded_percent = round(percent, 2)
    print(f"{letter} is {rounded_percent}% of the letters")
    #print(f"{letter}: {found_letters}   total: {total_letters}")


book_url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
the_text = str(requests.get(book_url).content)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count_letter(the_text, letter)
    
    