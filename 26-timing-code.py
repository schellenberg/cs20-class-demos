import time

start_time = time.time()
for counter in range(0, 1000):
    print(counter)
end_time = time.time()

total = end_time - start_time
print(f"That took {total} seconds.")