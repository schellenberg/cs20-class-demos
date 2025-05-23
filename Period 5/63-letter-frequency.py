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
phrase = "Good afternoon!"
for letter in alphabet:
    letter_count(phrase, letter)
    

