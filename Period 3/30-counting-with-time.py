import time

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

#track how long this takes...
start_time = time.time()

for number in range(1, 6):
    print(number)
    time.sleep(1)
    
end_time = time.time()
time_used = end_time - start_time
print(time_used)


    