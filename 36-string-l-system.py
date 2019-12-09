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

def create_l_system(axiom, level):
    transformed_string = axiom
    for counter in range(level):
        transformed_string = process_string(transformed_string)
    return transformed_string

print(create_l_system("A", 5))