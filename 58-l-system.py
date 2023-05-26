def apply_rules(letter):
    if letter == "A":
        return "B"
    
    elif letter == "B":
        return "AB"
    
    else:
        return letter

def process_string(some_string):
    transformed_string = ""
    for letter in some_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(iterations, axiom):
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

#testing
print(create_l_system(5, "A"))

