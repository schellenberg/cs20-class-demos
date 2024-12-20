message = "have a great break!"
# message = message.capitalize()
# message = message.upper()
# message = message.title()
# print(message.count("a"))
# print(message)

words = message.split()
new_message = ""
for word in words:
    word = word.capitalize()
    new_message = new_message + word + " "
    
print(new_message)
