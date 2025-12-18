def apply_rules(letter):
    '''Apply the rules to one letter, and return the result.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to every letter in the_string, and
       return the result.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    '''Start with the axiom, then apply the rules number_of_iterations
       times, and return the result.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string

print(create_l_system("A", 25))

