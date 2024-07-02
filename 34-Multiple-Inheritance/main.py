class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The Dance is {self.dance}")

# class DancerEmpoyee(Employee, Dancer): The order of the arguments in multiple inheritance MATTERS

class DancerEmpoyee(Dancer, Employee):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

obj = DancerEmpoyee("Atharva", "Classical")

obj.show()
print(DancerEmpoyee.mro()) 