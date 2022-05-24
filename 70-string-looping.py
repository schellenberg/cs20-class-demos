word = "competition"

#iterating by value
# for letter in word:
#     if letter in "aeiou":
#         print(letter)

#iterate by location
for index in range(len(word)):
    if index % 2 == 0:
        print(word[index])
