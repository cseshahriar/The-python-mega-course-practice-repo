""" Syntax errors """

"""
print(1)
int(9)
int 9  
print(2)
print 3
"""

print(1)
int(9)
int(9)  # int is function
print(2)
print(3)  # print is function

""" Exceptions (logical errors)"""
a = 1
b = "2"
c = 3
print(int(2.5))
print(a + float(b))
print(c)

""" try catch """
try:
    z = c / 0
except ZeroDivisionError:
    z = 0
print(z)


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is meaningless"


res = divide(1, 0)
print(res)
