people = ["Lacon", "Daniel", "John", "Chuyan"]

# people.clear()
people.append("Afrukhta")
people.append("Zara")
people.append("Mehreeb")

# people.sort()
# people.reverse()

someone = people.pop()
other = people.pop()

# print(people)
# print(other)

glue = ", "
the_people = glue.join(people)
print(the_people)


