import time

#time since the unix epoch...
# now = time.time()
# print(now)

start = time.time()
for counter in range(10):
    print(counter)
    counter = counter + 1
    time.sleep(0.5)
end = time.time()

how_long = end - start
print(f"That took {how_long} seconds.")
