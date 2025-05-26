def apply_rules(letter):
    '''Applies the rules to a single letter and returns it.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter
    
def process_string(some_string):
    '''Apply the rules to each letter in a string, and return the result.'''
    next_string = ""
    for letter in some_string:
        next_string = next_string + apply_rules(letter)
    return next_string

def create_l_system(iterations, axiom):
    '''Start with the axiom, then apply the rules iteration times.'''
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

print(create_l_system(15, "A"))
