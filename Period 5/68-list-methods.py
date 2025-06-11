people = ["Natasha", "Obontie", "Noor"]

people.append("Grayer")
people.append("Shiv")
people.append("Gavin")
people.append("Ayrton")
people.append("Feng")

people.sort()
people.reverse()

print(people)
someone = people.pop()
other_person = people.pop()

print(people)
print(other_person)
# print(len(people))

people.remove("Noor")
print(people)

glue = ", "
the_people = glue.join(people)
print(the_people)
