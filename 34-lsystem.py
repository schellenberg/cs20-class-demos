def apply_rules(letter):
    #rule 1
    if letter == "A":
        new_string = "B"
    
    #rule 2
    elif letter == "B":
        new_string = "AB"
    
    else:
        new_string = letter
    
    return new_string

def process_string(original_string):
    transformed_string = ""
    for letter in original_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string
    
def create_L_system(number_of_iterations, axiom):
    system_string = axiom
    for counter in range(number_of_iterations):
        system_string = process_string(system_string)
    return system_string


print(create_L_system(8, "A"))