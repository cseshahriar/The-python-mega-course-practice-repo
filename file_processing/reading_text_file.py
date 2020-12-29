""" Reading a text file """
# my_file = open("file_processing/fruits.txt") # obj 
# content = my_file.read() # content is corsor 
# my_file.close() # file must close 
# print(content)

""" file reading with context manager """
with open("file_processing/fruits.txt") as myfile:
    content2 = myfile.read()

print(content2)

""" new file writing """
# help(open())
with open("file_processing/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")


""" existing file writing """
with open("file_processing/fruits.txt", "a+") as myfile:
    myfile.write("\nOkra") # overrided file (a)
    myfile.seek(0) # zero position
    content3 = myfile.read() # (a+)

print(content3)