the_list = []

the_list.append(42)
the_list.append(60)
the_list.append(10)
the_list.insert(1, 50)
the_list.insert(3, 100)
the_list.sort()  #only works if all numbers (or if you do clever things)
last = the_list.pop()
the_list.remove(42)
print(the_list)