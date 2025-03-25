import FreeSimpleGUI as sg

# sg.popup("Hello there, CS20!")
# name = sg.popup_get_text("What is your name?", title="Name")

def popup_get_choice(options, title = "Make a Choice"):
    '''Use this function to allow users to select an option from a list.
    Pass in the options to choose from as a list.'''
    layout = [[sg.Listbox(options, size=(30, None), key="-LISTBOX-")],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    event, values = sg.Window(title, layout).read(close=True)

    if event == "Ok":
        try:
            return values["-LISTBOX-"][0]
        except:
            return None
    else:
        return None

# Use something similar to the following when using the popup_get_choice function
subjects = ["English", "Math", "Computer Science", "History", "Phys Ed"]
favourite = popup_get_choice(subjects)