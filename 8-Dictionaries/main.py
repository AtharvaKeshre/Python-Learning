# dic = {
#     1: "Atharva",
#     2: "Amisha"
# }
# print(dic[1])

# print(dic.get(3))
# # print(dic[3])

# for key in dic.keys():
#     print(f"The value is corresponding to {key} is {dic[key]}")


ep1 = {1: 100, 2: 89, 3: 60}
ep2 = {4: 64, 5:90}

ep1.update(ep2)
print(ep1)

ep1.pop(5)
print(ep1)

del ep1[1]
print(ep1)

