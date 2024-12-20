message = "have a great break!"
# message = message.capitalize()
# message = message.upper()

the_words = message.split()
new_message = ""
for word in the_words:
    word = word.capitalize()
    new_message = new_message + word + " "
print(new_message)