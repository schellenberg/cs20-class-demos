#from a string to a list
sentence = "my goodness it is cold outside"
words = sentence.split()

for index in range(len(words)):
    words[index] = words[index].capitalize()


#from a list to a string
glue = " "
new_sentence = glue.join(words)
print(new_sentence)