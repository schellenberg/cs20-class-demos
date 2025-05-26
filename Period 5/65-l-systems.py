def apply_rules(letter):
    '''Apply the rules to a letter and return the result.'''
    if letter == "A":
        return "B"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(some_string):
    '''Apply the rules to every letter in the string, and return the result.'''
    result = ""
    for letter in some_string:
        result = result + apply_rules(letter)
    return result

def create_l_system(iterations, axiom):
    '''Start with the axiom and apply the rules iterations times.'''
    result = axiom
    for counter in range(iterations):
        result = process_string(result)
    return result

print(create_l_system(5, "A"))
