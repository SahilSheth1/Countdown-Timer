# Importing libraries

import time

# Prompt for user to enter time

myTime = int(input("Enter the time in seconds: "))

# For loop for countdown timer process

for x in range(myTime, 0, -1):
    seconds = x % 60 # Convert time to seconds
    minutes = int(x / 60) % 60 # Convert time to minutes
    hours = int(x / 3600)  # Convert time to hours
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # Print in time format
    time.sleep(1) # Time sleep function

# Prints when time is done

print("TIME IS UP")