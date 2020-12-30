""" third party module """
import os
import time
import pandas # packages 


while True:
    if os.path.exists("builtin_module/temps.csv"):
        data = pandas.read_csv("builtin_module/temps.csv")
        print(data.mean())
        # print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(10) # outside of if, else