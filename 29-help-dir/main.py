import random

x = [1,2,3,4,5]
# print(dir(x))
# print(x.pop)


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e1 = Employee("Atharva", 100000)

print(e1.__dict__)

# print(help(Employee))

print(help(random))