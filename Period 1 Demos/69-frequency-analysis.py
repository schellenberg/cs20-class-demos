the_text = "Walter Murray is a good school"

def count_letters(text, letter):
    '''Return the percentage that letter shows up in text.'''
    times_seen = 0
    for character in text:
        if character == letter:
            times_seen = times_seen + 1
    
    print(f"{letter} shows up {times_seen} times")

count_letters(the_text, "c")