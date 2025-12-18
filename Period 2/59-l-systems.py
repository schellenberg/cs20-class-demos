def apply_rules(letter):
    '''Apply rules to one letter, and return result.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter
    
def process_string(the_string):
    '''Apply rules to every letter in a string, and return the result.'''
    transformed_string = ""
    for letter in the_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(number_of_iterations, axiom):
    '''Start with the axiom, then apply the rules number_of_iterations
       times. Return the result.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string

print(create_l_system(20, "A"))
        
    
    
    