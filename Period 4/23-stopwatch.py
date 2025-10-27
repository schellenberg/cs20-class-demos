import time

start = time.time()

for counter in range(1000):
    print(counter)

print()

end = time.time()

how_long = end - start
print(how_long)