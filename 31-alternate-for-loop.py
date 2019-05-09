school = "Walter Murray Collegiate"

new_school = ""
for counter in range(len(school)):
    letter = school[counter]
    if letter not in "aeiouy":
        new_school = new_school + letter

print(new_school)
