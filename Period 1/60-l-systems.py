def apply_rules(letter):
    '''Apply the rules to an individual letter.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to the_string, one letter at a time.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_L_system(iterations, axiom):
    '''Start with the axiom, and apply the rules iterations times.'''
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

print(create_L_system(5, "A"))
    
    
    