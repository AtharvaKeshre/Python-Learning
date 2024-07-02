# def cube(x):
#     return x**3

# lst = [1,2,3,4,5,6,7,8,9]

# newL = list(map(cube,lst))

# print(newL)


# filtered_list = list(filter(lambda x: x>4, lst))

# print(filtered_list)

from functools import reduce

n = [2,2,2]

reduced = reduce(lambda x,y: x**y, n)
print(reduced)