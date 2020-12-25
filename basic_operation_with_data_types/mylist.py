""" list """
monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(8.1)
print(monday_temperatures)
monday_temperatures.clear()
print(monday_temperatures)
# print(dir(list))

""" list index """
# help
# print(help(list))
# print(help(list.index))
my_list = [9.1, 8.8, 7.5]
my_list.append(3.3)
index_data = my_list.index(8.8)
print(index_data)
index_data = my_list.index(3.3, 2)  # start from index 2
print(index_data)

""" list items """
# help(list)
my_list = [9.1, 8.8, 7.5]
list_access = my_list[1]
list_access2 = my_list.__getitem__(1)
print(list_access, list_access2)

""" list slices """
print("list slices")
my_list = [9.1, 8.8, 7.5, 3.3, 5.5, 7.7]
print(my_list[3])  # index 3
print(my_list[1:4])  # index 1 to < 4
print(my_list[0:2])  # index 0 to < 2
print(my_list[:2])  # shortcut, index 0 to < 2
print(my_list[3:])  # shortcut, from index of 3 means 3 to last
print(my_list[-1])  # last item

# python list two index positive and negative
print("negative index")
my_list = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3, 4, 5]
#          1  2  3  4  5
#         -5 -4 -3 -2 -1
print(my_list[-3])
# upper limit not included
print(my_list[-4:-2])  # start from -3 to -4

""" string slices """
print("String slices ")
my_string = 'hello'
print(my_string[1])
print(my_string[-1])
print(my_string[:3])

my_list = ['hello', 1, 2, 3, 4, 5]
print(my_list[0])
print('--')
print(my_list[0][4])  # zero list index and 4 item index

""" does dict is have index ? """
# nope
print("dict")
my_dict = {
    "marry": 9.1,
    "sim": 8.8,
    "john": 7.5
}
print(my_dict['marry'])
