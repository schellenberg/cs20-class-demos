def apply_rules(letter):
    '''Apply the rules to a letter, and return the result.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to each letter in a string, and
       return the result.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, iterations):
    '''Start with the axiom, then apply the rules to string
       number of iterations times. Return the result.'''
    the_string = axiom
    for counter in range(iterations):
        the_string = process_string(the_string)
    return the_string

print(create_l_system("A", 5))
