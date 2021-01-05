a = 'Hello'

""" len """
string_len = len(a)
print(string_len)

""" upper """
str_upper = a.upper()
print(str_upper)

""" abs """
print(abs(-4/3))
print(abs(-11))
print(abs(11))

""" round """
print(round(-4/3))
print(round(1.49))
print(round(1.50))

""" min, max, sorted """
print(min(3, 2, 5))
print(max(3, 2, 5))
print(sorted([3, 2, 5]))

""" sum """
print(sum([3, 2, 1]))

""" The most important built-in Python methods """
str_lower = a.lower()
print(str_lower)

str_upper2 = a.upper()
print(str_upper2)

a = '   mug    '
str_strip = a.strip()
print(str_strip)

str_replace = a.replace('g', 'h')
print(str_replace)

b = 'Hello World'
str_split = b.split(' ')
print(str_split)

str_join = ' '.join(b)
print(str_join)

""" all , returns true if the iterable object is empty """
my_list = [0, 2, 2]
a = all(my_list)
print(a)

""" any , returns False if iterable is empty """
my_tuple = (0, 1, False)
a = any(my_tuple)
print(a)

""" Methods for Python Lists """
dog = ['Freddie', 9, True, 1.1, 2001, ['bone', 'little ball']]
dog.append(4)

print(dog)
dog.remove(2001)
print(dog)

print(dog.count('Freddie'))
dog.clear()
print(dog)

""" The delattr() function help us to remove the defined attribute from the declared object. """

print('delattr')


class User:
    name = "Jaydon"
    mob = 182182922
    country = "Canada"


delattr(User, 'name')
print(User)

"""  getattr() This function gets the value of the defined attribute from the particular object """

print("getattr")


class Student:
    name = "Ann"
    age = 28
    country = "USA"


x = getattr(Student, 'age')

print(x)

x = hasattr(Student, 'age')
print(x)

print(divmod(6, 2))

""" Methods for Python Dictionaries """
dog_dict = {
    'name': 'Freddie',
    'age': 9,
    'is_vaccinated': True,
    'height': 1.1,
    'birth_year': 2001,
    'belongings': ['bone', 'little ball']
}

print(dog_dict.keys())
print(dog_dict.values())
print(dog_dict.items())
print(dog_dict.clear())
