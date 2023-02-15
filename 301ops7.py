# ops 301 challenge 7
# Author Paul Thomas
# Date 2-14-23

# Import libraries
import os

# Assign to a variable a list of ten string elements.
my_produce_list = [ "carrot", "celery", "spinach", "squash", "potato", "turnip", "avocado", "apple", "orange", "lime" ]

# Print the fourth element of the list.
print(my_produce_list[3])

# Print the sixth through tenth element of the list.
sub = slice(5, 10)
print(my_produce_list[sub])

# Change the value of the seventh element to “onion”.
my_produce_list[6] = "onion"
print(my_produce_list)

### Read user input here into a variable
my_dir = input("Please input file path: ")

# Define Function
def dir_walk():
    print("***********Print Start***********")
    for (root_dir_path, sub_dirs, files) in os.walk(my_dir):
        
        ### Add a print command here to print ==root==
        print(root_dir_path)
        
        ### Add a print command here to print ==dirs==
        print(sub_dirs)
        
        ### Add a print command here to print ==files==
        print(files)
        
        ## Add line between returns
        print("*" * 25)
    print("***********Print End***********")
    
# Call Function
dir_walk()