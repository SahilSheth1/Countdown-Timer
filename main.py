import time

myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1)

print("TIME IS UP")