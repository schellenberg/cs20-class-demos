# CCC 2022 - J3 - Harp Tuning

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SIGNS = "+-"

tuning = input()

instructions = []

#parse instructions into a list of tunings
letters_start_at = 0
have_hit_sign = False

for index, letter in enumerate(tuning):
    if letter in SIGNS:
        have_hit_sign = True
    #at start of new instruction, so put the last one into the list
    elif letter in LETTERS and have_hit_sign == True:  
        this_instruction = tuning[letters_start_at:index]
        instructions.append(this_instruction)
        
        #reset for the next one
        letters_start_at = index
        have_hit_sign = False
        
#at end of the instructions set, so add the last one to the list
this_instruction = tuning[letters_start_at:]
instructions.append(this_instruction)

# print(instructions)

#make it human readable
for task in instructions:
    if "+" in task:
        plus_location = task.index("+")
        message = f"{task[:plus_location]} tighten {task[plus_location+1:]}"
    elif "-" in task:
        minus_location = task.index("-")
        message = f"{task[:minus_location]} loosen {task[minus_location+1:]}"
        
    print(message)