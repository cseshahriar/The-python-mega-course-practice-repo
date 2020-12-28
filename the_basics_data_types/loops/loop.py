""" loop """
monday_temp = [9.1, 8.8, 7.7]

# print(round(monday_temp[0]))

""" builtins functions """
# print(dir(__builtins__))

""" lopping a list """
for temprature in monday_temp:
    print(round(temprature))

""" string looping """
for latter in "Hello":
    print(latter)

""" lopping through a dict"""
my_dict = {
    "marry": 9.2,
    "sim": 8.8,
    "john": 7.5
}
# items(), keys, values 
for grade in my_dict.items(): 
    """ items() return key pare tuples """
    print(grade)


""" while loop """
username = ''
while username != 'pypy':
    username = input("Enter username: ")

while True:
    myname = input("Enter username: ")
    if myname == 'pypy':
        break # stop
    else:
        continue # jump or skip current loop