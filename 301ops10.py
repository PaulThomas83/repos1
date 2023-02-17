# ops 301 challenge 10
# Author Paul Thomas
# Date 2-16-23

# Create a new file if it does not exist
f = open("demofile.txt", "a")

# append 3 lines to file
f = open("demofile.txt", "a") 
with open("demofile.txt", "a") as f:
    l1 = "This is line 1\n"
    l2 = "This is line 2\n"
    l3 = "This is line 3\n"
f.writelines([l1, l2, l3])

# print to screen the first line
f = open("demofile.txt", "r")
print(f.readline())

# delete the .txt file
import os
os.remove("demofile.txt")