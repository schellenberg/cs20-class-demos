def letter_count(letter, text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    letter_count = 0
    total_letters = 0
    
    for character in text:
        if character in alphabet:
            total_letters += 1
            if character == letter:
                letter_count += 1
    
    percent = (letter_count / total_letters) * 100
    percent = round(percent, 2)
    print(f"{letter} - {percent}% of the text")

def frequency_analysis(text):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        letter_count(letter, text)
        
frequency_analysis("walter murray collegiate")