"""
Python is mainly used for automation purposes, web apps, and data science. Many big companies, like Instagram, Facebook, and Amazon, use Python in different parts of their products.
 For example, Facebook uses Python to process images.
"""

""" variables  """
import datetime
mynow = datetime.datetime.now()
print(mynow)

mynumber = 10
mytext = "Hello"

print(mynumber, mytext)

""" datatypes """
x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

""" list, list mutable or changable"""
student_grades = [9.1, 8.8, 7.5]
student_grades.append(5.5)

list_sum = sum(student_grades)
print("list sum is : ", list_sum)

length = len(student_grades)
print("list length is ", length)

""" type attrs and list functions """
# print(dir(list))

""" builtins """
print("builtins functions")
# print(dir(__builtins__))

""" help """
# dir(dict)
# help(dict.values)

print("hello".upper())


""" dict """
# list are more convinion for fraction values
temperatures = [9.1, 8.8, 7.5]
l_sum = sum(temperatures)
l_length = len(temperatures)
print(l_sum)

dict_grades = {"Marry": 9.1, "sim": 8.8, "Jhon": 7.5}
dict_values = dict_grades.values()
dict_keys = dict_grades.keys()
dict_sum = sum(dict_values)
print(dict_values)
print(dict_keys)
print(dict_sum)


""" tuple """
# immutable or not changable
monday_temp = (1, 4, 5)


""" how to user datatypes """
