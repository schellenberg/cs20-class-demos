def apply_rules(letter):
    '''Apply rule to a single letter and return the result.'''
    #rule 1
    if letter == "A":
        return "B"
    
    #rule 2
    elif letter == "B":
        return "AB"
    
    #not a rule, so just send it back unchanged
    else:
        return letter
    
def process_string(the_string):
    '''Apply the rules to every letter in an entire string, and return it.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    '''Start with the axiom, then apply the rules number_of_iterations times.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string    

print(create_l_system("A", 3))
        
        
        