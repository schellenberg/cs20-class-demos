import time

# print("something")
# time.sleep(2)
# print("another thing")

# print(1)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(3)
# time.sleep(1)
# print(4)
# time.sleep(1)
# print(5)
# time.sleep(1)

start_time = time.time()

for counter in range(1, 11):
    print(counter)
    time.sleep(1)

end_time = time.time()
how_long = end_time - start_time
print(f"It took {how_long} seconds.")

    