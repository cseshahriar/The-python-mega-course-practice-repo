""" collections: Counter, namedtuple, OrderedDict, defaultdict, deque """
from collections import Counter, namedtuple, OrderedDict, deque

""" counter """
a = 'aabbccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(list(my_counter.elements()))


""" namedtuple : lightweight object """
Point = namedtuple('Point', 'x,y')  # create a class
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

""" OrderedDict """
ordered_dict = OrderedDict()  # lower py 3.7 v
ordered_dict['b'] = 2
ordered_dict['a'] = 5
ordered_dict['c'] = 3
ordered_dict['d'] = 1
ordered_dict['e'] = 4
print(ordered_dict)

""" deque """
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()  # remove left
d.clear()
d.extend([4, 5, 6])
print(d)
