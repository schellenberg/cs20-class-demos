def change_character(letter):
    #rule 1
    if letter == "A":
        return "B"
    
    #rule 2
    elif letter == "B":
        return "AB"
    
    #catch all
    else:
        return letter
    
def convert_string(some_string):
    new_string = ""
    for letter in some_string:
        new_string = new_string + change_character(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    l_system = axiom
    for counter in range(number_of_iterations):
        l_system = convert_string(l_system)
    return l_system

print(create_l_system("A", 5))
        
        