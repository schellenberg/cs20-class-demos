def apply_rules(some_letter):
    if some_letter == "A":
        return "B"
    elif some_letter == "B":
        return "AB"
    else:
        return some_letter

def process_string(original_string):
    converted_string = ""
    for letter in original_string:
        converted_string = converted_string + apply_rules(letter)
    return converted_string

def create_l_system(axiom, level):
    converted_string = axiom
    for counter in range(level):
        converted_string = process_string(converted_string)
    return converted_string

print(create_l_system("A", 3))