import time

myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1):
    print(x)
    time.sleep(1)

print("TIME IS UP")