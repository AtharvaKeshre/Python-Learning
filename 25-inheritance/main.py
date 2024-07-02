class Employee:
    def __init__(self,name,emp_No):
        self.name = name
        self.emp_no = emp_No

    def emp_name(self):
        print(f"Name = {self.name}")

    def emp_id(self):
        print(f"Emp_ID = {self.emp_no}")

class Programmer(Employee):
    def __init__(self, name, emp_no):
        super().__init__(name, emp_no)
        print(f"This person is a developer: {self.name}")


Atharva = Employee("Atharva",1)
Atharva.emp_id()
Atharva.emp_name()
ak = Programmer("Ath", 2)
ak.emp_id()
ak.emp_name()
