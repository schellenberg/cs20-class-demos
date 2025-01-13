# things = ["ben", 42, False]
# print(things[1])
# print(len(things))

# some_other = [15, "jon", ["Murray", "Cross", "Beth"]]
# print(some_other[2][0][1])
# print(len(some_other))

# the_list = ["a", "b", "c", "d", "e", "f"]
# print(the_list[2:5])
# print("x" not in the_list)

# lists are mutable -- you CAN change them
# fruit = ["apple", "banana", "cherry"]
# fruit[1] = "orange"
# print(fruit)

# strings are immutable -- you CANNOT change them
# greeting = "Hello world!"
# greeting[0] = "J"
# print(greeting)

people = ["Kamal", "Sohaib", "Audrey", "Owen", "Jon"]
# for person in people:
#     print(f"Hello there {person}!")

for index in range(len(people)):
    print(f"Hello there {people[index]}!")

