# The python mega course practice repository

Did you know The <strong>Python</strong> is mainly used for <strong>automation purposes</strong>, <strong>web apps</strong>, and <strong>data science</strong>. Many big companies, like Instagram, Facebook, and Amazon, use Python in different parts of their products. For example, <strong>Facebook</strong> uses Python to <strong>process images</strong>.

Did you know That <strong>Python</strong> was first released in 1991? <strong>Python 2</strong> was released in 2000, and Python 3 (the current version) in 2008.

Did you know The Python got his name not from the snake, but from <strong>Monty Python's Flying Circus</strong>, a favorite comedy series of <strong>Guido van Rossum</strong>, the <strong>creator of Python</strong>.

Did you know The <strong>Python</strong> comes pre-installed on <strong>Linux</strong> and <srong>Mac<//srong> operating systems. In May 2019, Windows 10 also launched an update that also has Python pre-installed. That is an added endorsement for Python.

Did you know The <strong>Python</strong> was the sixth most popular programming language in 2010 on <strong>StackOverflow</strong>. It continually went up in the ranks to be the most popular among all in <strong>2018</strong>


## The basics of Python

In this section, you learned that:
<br>

Integers are for representing whole numbers:
<pre>
rank = 10
eggs = 12
people = 3
</pre>
<br>

Floats represent continuous values:
<pre>
temperature = 10.2
rainfall = 5.98
elevation = 1031.88
</pre>
<br>

Strings represent any text:
<pre>
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
</pre>
Lists represent arrays of values that may change during the course of the program:

<pre>
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
</pre>
<br>

Dictionaries represent pairs of keys and values:
<pre>
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
</pre>
<br>

Keys of a dictionary can be extracted with:
<pre>
phone_numbers.keys()
Values of a dictionary can be extracted with:
</pre>

<pre>
phone_numbers.values()
</pre>
Tuples represent arrays of values that are not to be changed during the course of the program:

<pre>
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:
</pre>

<pre>
dir(str)
dir(list)
dir(dict)
  
 help(list)
 help(list.values)
</pre>
To find out what Python builtin functions there are:

<pre>
dir(__builtins__)
</pre>
Documentation for a Python command can be found with:

<pre>
help(str)
help(str.replace)
help(dict.values)
</pre>


## Function
In this section, you learned to:

Define a function:
<pre>
def cube_volume(a):
    return a * a * a
Write a conditional block:

message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")
Write a conditional block of multiple conditions:

message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
</pre>

Use the and operator to check if both conditions are True at the same time:

<pre>
x = 1
y = 1

if x == 1 and y==1:
    print("Yes")
else:
    print("No")
</pre>
Output is Yes since both x and y are 1.

Use the or operator to check if at least one condition is True:
<pre>
x = 1
y = 2

if x == 1 or y==2:
    print("Yes")
else:
    print("No")
</pre>

Output is Yes since x is 1.

Check if a value is of a particular type with:
<pre>
isinstance("abc", str)
isinstance([1, 2, 3], list)
</pre>

or
<pre>
type("abc") == str
type([1, 2, 3]) == lst
</pre>

## User input and String formating
In this section, you learned that:

A Python program can get user input via the input function:

The input function halts the execution of the program and gets text input from the user:

<pre>
name = input("Enter your name: ")
</pre>

The input function converts any input to a string, but you can convert it back to int or float:

<pre>
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
</pre>
You can format strings with (works both on Python 2 and 3):

<pre>
name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
</pre>
Output: Hi Sim, you have 1.5 years of experience.

You can also format strings with:
<pre>
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
</pre>
Output: Hi Sim, you have 1.5 years of experience.

## Looping
In this section, you learned that:

For loops are useful for executing a command over a large number of items.

You can create a for loop like so:
<pre>
for letter in 'abc':
    print(letter.upper())
</pre>
Output:

A
B
C

The name after for (e.g. letter) is just a variable name



You can loop over dictionary keys:
<pre>
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
</pre>
Output:

John Smith
Marry Simpsons

You can loop over dictionary values:
<pre>
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
</pre>
Output:

+37682929928
+423998200919

You can loop over dictionary items:
<pre>
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
</pre>
Output: 

('John Smith', '+37682929928')

('Marry Simpons', '+423998200919')


While loops will run as long as a condition is true:
<pre>
while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
</pre>
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.

## Comprehension
In this section, you learned that:

A list comprehension is an expression that creates a list by iterating over another container.

A basic list comprehension:
<pre>
[i*2 for i in [1, 5, 10]]
Output: [2, 10, 20]
</pre>
List comprehension with if condition:
<pre>
[i*2 for i in [1, -2, 10] if i>0]
Output: [2, 20]
</pre>
List comprehension with an if and else condition:
<pre>
[i*2 if i>0 else 0 for i in [1, -2, 10]]
Output: [2, 0, 20]
</pre>

## More Function 
In this section, you learned that:

Functions can have more than one parameter:

<pre>
def volume(a, b, c):
    return a * b * c
</pre>
Functions can have default parameters (e.g. coefficient):

<pre>
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters

print(converter(10))
</pre>
Output: 3.0480370641306997

Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):
<pre>
def volume(a, b, c):
    return a * b * c

print(volume(1, b=2, c=10))
</pre>
An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:
<pre>
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
</pre>
Output: 1001

An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
<pre>
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)

print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
</pre>
Output: Sim

Here's a summary of function elements:

## file reading and writing 
In this section, you learned that:

You can read an existing file with Python:
<pre>
with open("file.txt") as file:
    content = file.read()
</pre>
You can create a new file with Python and write some text on it:

<pre>
with open("file.txt", "w") as file:
    content = file.write("Sample text")
</pre>
You can append text to an existing file without overwriting it:

<pre>
with open("file.txt", "a") as file:
    content = file.write("More sample text")
</pre>
You can both append and read a file with:

<pre>
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
</pre>