""" functions """
def mean(value):
    """
    isinstance(object, type)
    The isinstance() function returns True if the specified object is of 
    the specified type, otherwise False
    """
    if isinstance(value == dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

my_list = [1, 2, 3, 4, 5, 6]
print(mean(my_list))

""" print or none """
# by default return none
def mean_another(my_list):
    the_mean = sum(my_list) + len(my_list)
    # print(the_mean) # wrong
    return the_mean
mymean = mean_another([0, 3, 4])
print(mymean + 10) # unsupported operand type(s) for +: 'NoneType' and 'int'

# always use return for function, not print


""" use of white spaces """
if    3 > 1: # wrong
    print('a')

    print('aa')
    print('aaa')

if 3>1: # worng
    print('b')

print('bb')
print('bbb')

# correct
if 3 > 1:
    print('c')
    # break line for if S
print('cc')
print('ccc')
# break line
def foo():
    pass