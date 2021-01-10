"""
পাইথনের ভাষায়, ডেকোরেটর হল এমন একটা ফাংশন যা অন্য কোন ফাংশনের কার্যপরিধি কোন
 প্রকার মডিফিকেশন ছাড়াই এক্সটেন্ড করে। 
"""
from time import time


def print_int(my_function):
    """ print_int return any_function """

    def any_function():
        """ any_function return arg function """
        return my_function

    return any_function()


@print_int
def get_int_as_str(number):
    print(str(number))
    return


get_int_as_str(130)

""" less execution time """


def timer(any_function):
    def count_time():
        start = time()
        any_function()
        stop = time()
        print(stop - start, 'seconds')
        return
    return count_time


@timer
def hello():
    print('Hello World')
    return


@timer
def another_function():
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(item)
    return


hello()
another_function()
