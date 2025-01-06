def apply_rules(letter):
    '''Apply the rules to a single letter and return the result.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to a string, one letter at a time, and
       return the result.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, iterations):
    '''Start with the axiom, then apply the rules iterations times.
       Return the result.'''
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

print(create_l_system("A", 15))
    

