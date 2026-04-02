import time

#if you want to test how long something takes
start_time = time.time()

for counter in range(5, 0, -1):
    print(counter)
    time.sleep(1)
    
print("Blastoff!")
    
end_time = time.time()

total_time = end_time - start_time
print(f"That took {total_time} seconds.")