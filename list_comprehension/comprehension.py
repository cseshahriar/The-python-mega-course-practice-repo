""" Comprehension """
temps = [221, 234, -9999, 340, 230]

""" normal thing """
# new_temps = []
# for temp in temps:
#     new_temps.append(temp/10)

# print(new_temps)

""" batter solution """
list_compreshension = [temp / 10 for temp in temps]
print(list_compreshension)

""" comprehension with if else """
new_list = [temp / 10  if temp != -9999 else 0 for temp in temps]
print(new_list)
