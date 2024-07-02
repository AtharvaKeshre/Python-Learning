class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Harry", 12000)

string = "Atharva-12000"

e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
print(type(e2.salary))