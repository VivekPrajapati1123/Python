import time
print(time.time())

cr = time.time()
print(time.ctime(cr+3000))

for i in range(6):
    print(i)
    time.sleep(5) 