from math import remainder
# 1. String
# sting = "Hello World"
# string1 = "My name is PY!"
# def str_length(s):
#     return len(s)
#
# def str_join(s,x):
#     return f"{s}\n{x}"
#
# print(str_length(sting))
# print(str_join(sting,string1))

# 2. Integer and float
# def square(x):
#     return f"square = {x * x}"
# print(square(3))
# print(square(4))
#
# def sum(x, n):
#     return f"sum = {x + n}"
# print(sum(3,4))
#
# def divide_int(x: int, y: int):
#     w = x // y
#     r = x % y
#     return f"whole part = {w}, remainder = {y}"

# print(divide_int(5,4))

# 3. Lists
# l = (2,3,6,78,9,76,4)
# l2 = (2,4,6,77,8,76)

# def average_value(x):
#     return sum(x) / len(x)
# print(average_value(l))

# def common_elements(a, b):
#     return list(set(a) & set(b))
# print(common_elements(l,l2))

# 4. Dictionaries
# d = {"name": "DC", "age": 34, "gender": "male", "hobby": "crossfit"}
# d1 = {"car": "BMW", "country": "Ukraine", "city": "Kyiv"}
# def dict_keys(x):
#     return list(x.keys())
#
# print(dict_keys(d))

# def connect_dict(dict1, dict2):
#     return dict1 | dict2
#
# print(connect_dict(d, d1))

# 5. Sets
# first_set = {1, 2, 3, 4, 5}
# second_set = {4, 5, 6, 7, 8}
# third_set = {1,3,4}

# def connect_set(set1, set2):
#     return set1.union(set2)
#
# print(connect_set(first_set, second_set))

# def sub_set(set1, set2):
#     return set1.issubset(set2) or set2.issubset(set1)
#
# print(sub_set(first_set, third_set))

# 6.
# def even_odd(num):
#     if num % 2 == 0:
#         print("Парне")
#     else:
#         print("Непарне")
#
# even_odd(6)

# def even_list(l):
#     res = list()
#     for i in l:
#         if i % 2 == 0:
#             res.append(i)
#     return res
#
# print(even_list([1,2,3,4,5,6,7,8,9,10]))

# 7. Lambda

# even_odd = lambda x: "Парне" if x % 2 == 0 else "Непарне"

# print(even_odd(5))
