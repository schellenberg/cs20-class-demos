def apply_rules(letter):
    #rule 1
    if letter == "A":
        return "B"
    
    #rule 2
    elif letter == "B":
        return "AB"
    
    #no rules apply
    else:
        return letter
    
def transform_string(some_string):
    new_string = ""
    for letter in some_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    the_string = axiom
    for counter in range(number_of_iterations):
        the_string = transform_string(the_string)
    return the_string

print(create_l_system("A", 15))
        
        