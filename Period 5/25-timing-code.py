import time

#timing my code
then = time.time()
for counter in range(10):
    print(counter)
    counter = counter + 1
    time.sleep(1.5)
now = time.time()
how_long = now - then
print(f"That took {how_long} seconds.")

