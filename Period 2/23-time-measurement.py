import time

start = time.time()

for counter in range(1000):
    print(counter)
    
end = time.time()

time_taken = end - start
print(time_taken)