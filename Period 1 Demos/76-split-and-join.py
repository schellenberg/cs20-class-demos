#converting back and forth from string to list

sentence = "boy it's cold outside!"
words = sentence.split()
#print(words)

for index in range(len(words)):
    words[index] = words[index].capitalize()

glue = " "
new_string = glue.join(words)
print(new_string)