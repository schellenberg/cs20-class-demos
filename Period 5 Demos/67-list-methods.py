people = ["noreen", "vijeta", "hao"]

# people.clear()

people.append("angus")
people.append("abedin")

number_of_times = people.count("vijeta")
# print(number_of_times)

location = people.index("angus")

people.insert(location, "joti")

name = people.pop(2)
print(name)

people.remove("joti")

people.reverse()

people.sort()

print(people)