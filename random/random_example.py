# Program to generate a random number between 0 and 9

# importing the random module
import random

""" return random int in range """
print(random.randint(0, 9))

""" return random int in range"""
print(random.randrange(1, 10))

""" return random float in range """
print(random.uniform(20, 30))

"""
To pick a random element from a non-empty sequence (like a list or a tuple),
you can use random.choice(). There is also random.choices() for choosing
multiple elements from a sequence with replacement (duplicates are possible):
"""

items = ['one', 'two', 'three', 'four', 'five']
print(random.choice(items))

print(random.choices(items, k=2))  # two val return

print(random.choices(items, k=3))  # three val return

"""
You can randomize a sequence in-place using random.shuffle().
This will modify the sequence object and randomize the order of elements:
"""
print(items)  # before
random.shuffle(items)
print(items)  # after shuffle
