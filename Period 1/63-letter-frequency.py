def letter_count(text, letter_to_find):
    '''Prints out the percentage of characters that are
       letter inside text.'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    occurances = 0
    total_letters = 0
    for letter in text.lower(): #convert everything to lowercase
        if letter in alphabet:
            total_letters += 1
        if letter == letter_to_find:
            occurances += 1
    percentage = occurances / total_letters * 100
    percentage = round(percentage, 2)
    print(f"{letter_to_find} - {percentage}%")
    
test_phrase = "Good morning, Computer Science 20!"

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    #write out the percentages for every letter
    letter_count(test_phrase, letter)




