# a = int(input("Enter value between 5 - 10 : "))

# if (a<5 or a>11):
#     raise ValueError("VAlue should be between 5 - 10")

# print(a) 

a = input("Enter value between 5 - 10 : ")
if(a=="quit"):
    pass
elif (a<5 or a>11):
    raise ValueError("VAlue should be between 5 - 10")

print(a) 

