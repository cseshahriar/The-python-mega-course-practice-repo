import time
import os

""" file did not found but execution not stop solution """
while True:
    if os.path.exists("builtin_module/file.txt"):
        with open("builtin_module/file.txt") as my_file:
            print(my_file.read())
    else:
        print("File does not exist")
    time.sleep(10) # outside of if, else