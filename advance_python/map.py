"""
The map() function executes a specified function for 
each item in an iterable. The item is sent to the function as a parameter.
"""


def square(n):
    return n * n


my_list = [2, 3, 4, 5, 6, 7, 8, 9]

map_list = map(square, my_list)
print(map_list)
print(list(map_list))


def myfunc(a, b):
    return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'),
        ('orange', 'lemon', 'pineapple'))
