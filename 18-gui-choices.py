import easygui_qt as easy

people = ["Macayla", "Aiden", "Andrew"]

eraser = easy.get_choice("Who is on for erasing the whiteboard?", "Eraser", people)

easy.show_message(eraser + " is on to clean the whiteboard.")