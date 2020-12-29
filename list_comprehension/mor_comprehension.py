"""
পাইথনে ইটারেটর তৈরি করার কিছু সহজ পদ্ধতি আছে। 
পাইথনিক ভাষায় এদের কম্প্রিহেনশন বলে। 
আরেকটু ভালোভাবে বলতে গেলে, 
কোনো একটা সিক্যুয়েন্স থেকে লিস্ট বা 
ডিকশনারির মতো ইটারেটর তৈরি করার 
পদ্ধতিই হলো কম্প্রিহেনশন। শুধু লিস্ট 
আর ডিকশনারিই নয়, সেটও তৈরি করা যায়। 
একটা কম্প্রিহেনশনে তিনটি পার্ট থাকে। এগুলো হলো-
"""
""" newlist = [expression for item in iterable if condition == True]"""

""" list comprehension """
my_list = [ i**2 for i in range(20) if i % 2 == 0]
print(my_list)

""" [expression for item in list] """
h_letters = [letter for letter in 'human']
print(h_letters)

num_list = [x for x in range(20) if x % 2 == 0]
print(num_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0 ]
print(num_list)

obj = ["Even" if i % 2 == 0 else "odd" for i in range(10)]
print(obj)

# nested 
matrix = [[1,2], [3,4], [5,6], [7,8]]
transpose = [ [row[i] for row in matrix] for i in range(2)]
print(transpose)