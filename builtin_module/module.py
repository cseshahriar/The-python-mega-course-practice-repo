""" bultin module """
# dir(str)
# dir(__builtins__)

username = "pypy"
print(len(username))

""" import """
import sys
import time
# print(sys.builtin_module_names)
# print(dir(time))
# print(help(time.sleep))

""" example """
while True:
    with open("builtin_module/file.txt") as file:
        print(file.read())
        time.sleep(10) # sec

""" python standard modules """