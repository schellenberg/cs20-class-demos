# people = ["Maysie", "Luca", "Kai", "Hanley", "Narayan", "Theo"]
# print(people[4][2])
# print(len(people))
# print("Luca" in people)
# print(people[0:3])

# people = [["Maysie"], ["Luca", "Kai"], ["Hanley", "Narayan", "Theo"]]
# print(len(people))
# print(people[2][0])
# print(people[2][0][-1])
# print("Luca" in people)


# people = ["Maysie", "Luca", "Kai", "Hanley", "Narayan", "Theo"]
# people[1] = "Apipa"
# print(people)

# greeting = "Hello world!"
# greeting[0] = "J"
# print(greeting)



people = ["Maysie", "Luca", "Kai", "Hanley", "Narayan", "Theo"]

#don't care about index
# for person in people:
#     print(person)

#do care about index
for index in range(len(people)):
    print(people[index])


